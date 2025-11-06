from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import (
    BaseMessage,
    AIMessage,
    SystemMessage,
)
from langchain.chat_models import init_chat_model

from langchain_mcp_adapters.resources import load_mcp_resources
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_mcp_adapters.client import BaseTool, ClientSession, MultiServerMCPClient

import sys
import asyncio
import logging

from os import getenv
from dotenv import load_dotenv
from rich.logging import RichHandler

from collections.abc import Sequence

from utils import asserted_env
from claims import ClaimHandler
from tools import ToolRunner

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(RichHandler(rich_tracebacks=True))

USD_PER_TOKEN = 0.000001

class InMemoryHistory:
    """In memory implementation of chat message history."""

    messages: list[BaseMessage]

    def __init__(self):
        self.messages = []

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        """Add a list of messages to the store"""
        self.messages.extend(messages)

    def add_message(self, message: BaseMessage):
        self.messages.append(message)

    def clear(self) -> None:
        self.messages = []


async def fetch_tools(
        client: MultiServerMCPClient, coral_session: ClientSession
) -> list[BaseTool]:
    """Helper to fetch all MCP tools from all servers, while reusing an already opened ClientSession for the Coral MCP server"""
    try:
        coral_tools = await load_mcp_tools(
            coral_session,
            connection=client.connections["coral"],
        )
        other_connections = list(
            filter(lambda k: k != "coral", client.connections.keys())
        )
        other_tools = []
        for server in other_connections:
            other_tools.extend(await client.get_tools(server_name=server))
        logger.info(f"Found {len(other_tools)} non-coral tools.")
        return coral_tools + other_tools
    except Exception as e:
        logger.exception("Failed to get MCP tools: %s", repr(e))
        sys.exit(1)


async def main():
    # What orchestration runtime we are running in (docker, executable, etc.). None if we aren't orchestrated (i.e. devmode)
    CORAL_RUNTIME = getenv("CORAL_ORCHESTRATION_RUNTIME", None)

    # Load .env file if we are in dev mode for convenience
    if CORAL_RUNTIME is None:
        _ = load_dotenv()

    # URL to the Coral MCP Server we need to connect to. This is provided by Coral Server when orchestrating us.
    CORAL_CONNECTION_URL = asserted_env("CORAL_CONNECTION_URL")

    # Load the Coral Server provided system prompt injection parameter passed in via orchestration
    EXTRA_PROMPT = getenv("CORAL_PROMPT_SYSTEM", "")

    # Load the rest of our options as defined in coral-agent.toml.
    # (we can assert these variables exist since Coral Server provides the default value for any non-required options)
    SYSTEM_PROMPT = asserted_env("SYSTEM_PROMPT")
    MODEL_NAME = asserted_env("MODEL_NAME")
    MODEL_PROVIDER = asserted_env("MODEL_PROVIDER")
    MODEL_API_KEY = asserted_env("MODEL_API_KEY")
    MODEL_BASE_URL = getenv("MODEL_BASE_URL")

    if MODEL_BASE_URL and MODEL_BASE_URL.upper() != "UNMODIFIED":
        kwargs = {"base_url": MODEL_BASE_URL}
    else:
        kwargs = {}

    TEMPERATURE = float(asserted_env("MODEL_TEMPERATURE"))
    MAX_TOKENS = int(float(asserted_env("MODEL_MAX_TOKENS")))

    MAX_ITERATIONS = int(float(asserted_env("MAX_ITERATIONS")))

    global claim_handler  # This is global so tools can use it easily
    claim_handler = ClaimHandler("usd")

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content=f"{{coral_instruction}} {SYSTEM_PROMPT} {EXTRA_PROMPT} {{coral_messages}}"
            ),
            MessagesPlaceholder("history"),
        ]
    )

    model = init_chat_model(
        model=MODEL_NAME,
        model_provider=MODEL_PROVIDER,
        api_key=MODEL_API_KEY,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        **kwargs
    )

    client = MultiServerMCPClient(
        connections={
            "coral": {
                "transport": "sse",
                "url": CORAL_CONNECTION_URL,
                "timeout": 300000,
                "sse_read_timeout": 300000,
            },
            "firecrawl-mcp": {
                "transport": "stdio",
                "command": "npx",
                "env": {
                    "FIRECRAWL_API_KEY": asserted_env("FIRECRAWL_API_KEY")
                },
                "args": ["-y", "firecrawl-mcp"]
            },
        }
    )

    history = InMemoryHistory()

    logger.info(f"Connecting to Coral @ '{CORAL_CONNECTION_URL}'")
    async with client.session("coral") as coral_session:
        tools = await fetch_tools(client, coral_session)
        chain = prompt | model.bind_tools(tools)
        tool_runner = ToolRunner(tools)

        logger.info("Fetching instruction resource...")
        coral_instruction = (
            await load_mcp_resources(coral_session, uris="coral://agent/instruction")
        )[0]

        for _ in range(MAX_ITERATIONS):
            if claim_handler.no_budget():
                logger.info("No more budget - breaking loop")
                break
            coral_messages = (
                await load_mcp_resources(coral_session, uris="coral://messages")
            )[0]

            logger.info("Making completion request...")
            step_result: BaseMessage = await chain.ainvoke(
                {
                    # We pass in our loaded resources here
                    # (as_string is safe here because we know these resources always return text)
                    "coral_instruction": [
                        SystemMessage(content=coral_instruction.as_string())
                    ],
                    "coral_messages": [
                        SystemMessage(content=coral_messages.as_string())
                    ],
                    # and our message history
                    "history": history.messages,
                }
            )

            # Claim cost per tokens used each step
            total_to_claim = 0.0
            total_tokens = 0
            try:
                total_tokens = step_result.model_dump().get("response_metadata").get("token_usage").get("total_tokens")
                total_to_claim = total_tokens * USD_PER_TOKEN
                logger.info(f"Total to claim for step: ${total_to_claim:.6f}")
            except AttributeError:
                total_to_claim = 0.0
                total_tokens = 0
                logger.warning("No response_metadata.token_usage.total_tokens"
                               " found on step result. Can't calculate token cost.")
            if total_to_claim > 0.0:
                claim_handler.claim(total_to_claim)
                logger.info(f"Claimed cost for step: ${total_to_claim:.6f} for {total_tokens} tokens")

            logger.info("-> '%s'", step_result.content)

            history.add_message(step_result)

            if isinstance(step_result, AIMessage):
                tool_calls = step_result.tool_calls
                for call in tool_calls:
                    history.add_message(await tool_runner.run_tool(call))


if __name__ == "__main__":
    asyncio.run(main())
