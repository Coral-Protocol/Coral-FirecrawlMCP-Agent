## [Firecrawl MCP Agent](https://github.com/Coral-Protocol/firecrawl-coral-agent.git)

The Firecrawl MCP Agent is an open-source agent built to perform advanced web scraping, crawling, and data extraction operations.

## Responsibility
The Firecrawl MCP Agent is an open-source agent designed for comprehensive web scraping, crawling, and data extraction tasks. It excels in structured data extraction and deep research by leveraging a multi-agent architecture to efficiently navigate, search, and analyze web content.


## Details
- **Framework**: LangChain
- **Tools used**: Firecrawl MCP Server Tools, Coral Server Tools
- **AI model**: OpenAI GPT-4o
- **Date added**: June 4, 2025
- **Reference**: [Firecrawl MCP Repo](https://github.com/mendableai/firecrawl)
- **License**: MIT

## Setup the Agent

### 1. Clone & Install Dependencies

<details>

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system. If you are trying to run Open Deep Research agent and require an input, you can either create your agent which communicates on the coral server or run and register the [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent) on the Coral Server  


```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/Coral-FirecrawlMCP-Agent.git

# Navigate to the project directory:
cd Coral-FirecrawlMCP-Agent

# Download and run the UV installer, setting the installation directory to the current one
curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=$(pwd) sh

# Create a virtual environment named `.venv` using UV
uv venv .venv

# Activate the virtual environment
source .venv/bin/activate

# install uv
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

</details>

### 2. Configure Environment Variables

<details>

Get the API Key:
[OpenAI](https://platform.openai.com/api-keys) || 
[Github Token](https://github.com/settings/tokens)

```bash
# Create .env file in project root
cp -r .env_sample .env
```

Check if the .env file has correct URL for Coral Server and adjust the parameters accordingly.

</details>

## Run the Agent

You can run in either of the below modes to get your system running.  

- The Executable Model is part of the Coral Protocol Orchestrator which works with [Coral Studio UI](https://github.com/Coral-Protocol/coral-studio).  
- The Dev Mode allows the Coral Server and all agents to be seperately running on each terminal without UI support.  

### 1. Executable Mode

Checkout: [How to Build a Multi-Agent System with Awesome Open Source Agents using Coral Protocol](https://github.com/Coral-Protocol/existing-agent-sessions-tutorial-private-temp) and update the file: `coral-server/src/main/resources/application.yaml` with the details below, then run the [Coral Server](https://github.com/Coral-Protocol/coral-server) and [Coral Studio UI](https://github.com/Coral-Protocol/coral-studio). You do not need to set up the `.env` in the project directory for running in this mode; it will be captured through the variables below.

<details>

For Linux or MAC:

```bash
registry:
  # ... your other agents
  firecrawlmcp_agent:
    options:
      - name: "MODEL_API_KEY"
        type: "string"
        description: "API key for the service"
      - name: "FIRECRAWL_API_KEY"
        type: "string"
        description: "FIRECRAWL API KEY for the service"
      - name: "MODEL_NAME"
        type: "string"
        description: "What model to use (e.g 'gpt-4.1-mini')"
        default: "gpt-4.1-mini"
      - name: "MODEL_PROVIDER"
        type: "string"
        description: "What model provider to use (e.g 'openai', etc)"
        default: "openai"
      - name: "MODEL_MAX_TOKENS"
        type: "string"
        description: "Max tokens to use"
        default: "16000"
      - name: "MODEL_TEMPERATURE"
        type: "string"
        description: "What model temperature to use"
        default: "0.3"
    runtime:
      type: "executable"
      command: ["bash", "-c", "<replace with path to this agent>/run_agent.sh main.py"]
      environment:
        - option: "MODEL_API_KEY"
        - option: "FIRECRAWL_API_KEY"
        - option: "MODEL_NAME"
        - option: "MODEL_PROVIDER"
        - option: "MODEL_MAX_TOKENS"
        - option: "MODEL_TEMPERATURE"

```
For Windows, create a powershell command (run_agent.ps1) and run:

```bash
command: ["powershell","-ExecutionPolicy", "Bypass", "-File", "${PROJECT_DIR}/run_agent.ps1","main.py"]
```

</details>

### 2. Dev Mode

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system and run below command in a separate terminal.

<details>

```bash
# Run the agent using `uv`:
uv run python main.py
```

You can view the agents running in Dev Mode using the [Coral Studio UI](https://github.com/Coral-Protocol/coral-studio) by running it separately in a new terminal.

</details>


## Example

<details>

```bash
# Input:
What is Model Context Protocol?

#Output:
The Model Context Protocol (MCP) is an innovative open-source standard designed to enhance the interaction between artificial intelligence (AI) models and external tools and data sources. Introduced by Anthropic in November 2024, MCP addresses a critical challenge in the AI space by enabling seamless integration among diverse applications, particularly large language models (LLMs). This protocol streamlines data sharing and context management, offering a cohesive framework that allows AI systems to access real-time information efficiently. By eliminating the need for custom integrations, MCP fosters a more dynamic and interconnected AI ecosystem, thus empowering developers to create responsive and context-aware applications.
```

</details>

### Creator Details
- **Name**: Suman Deb
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)

