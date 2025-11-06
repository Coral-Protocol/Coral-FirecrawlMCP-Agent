import logging
from rich.logging import RichHandler

from collections.abc import Sequence

from langchain_mcp_adapters.client import BaseTool
from langchain_core.messages import (
    ToolCall,
    ToolMessage,
)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(RichHandler(rich_tracebacks=True))


class ToolRunner:
    tool_by_name: dict[str, BaseTool]

    def __init__(self, tools: Sequence[BaseTool]) -> None:
        self.tool_by_name = {}
        for tool in tools:
            self.tool_by_name[tool.name] = tool

    async def run_tool(self, call: ToolCall) -> ToolMessage:
        if call["name"] == "":
            return ToolMessage(
                content=f"Failed to run tool - no tool name passed!",
                tool_call_id=call["id"],
            )
        tool = self.tool_by_name.get(call["name"], None)
        if tool is None:
            return ToolMessage(
                content=f"Failed to run tool - tool '{call["name"]}' not found",
                tool_call_id=call["id"],
            )
        try:
            tool_result = await tool.arun(call["args"])
            message = ToolMessage(content=tool_result, tool_call_id=call["id"])
            logger.debug("tool_result: %s", tool_result)
        except Exception as e:
            content = f"Error running tool '{call["name"]}' - {e}"
            logger.warning(content)
            return ToolMessage(content=content)
        return message
