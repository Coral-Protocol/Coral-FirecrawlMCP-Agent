## [Firecrawl Coral Agent](https://github.com/Coral-Protocol/firecrawl-coral-agent.git)

The Firecrawl Coral Agent is an open-source agent built to perform advanced web scraping, crawling, and data extraction operations.

## Responsibility
The Firecrawl Coral Agent is an open-source agent designed for comprehensive web scraping, crawling, and data extraction tasks. It excels in structured data extraction and deep research by leveraging a multi-agent architecture to efficiently navigate, search, and analyze web content.


## Details
- **Framework**: LangChain
- **Tools used**: Firecrawl MCP Server Tools, Coral Server Tools
- **AI model**: OpenAI GPT-4o
- **Date added**: June 4, 2025
- **Reference**: [Firecrawl MCP Repo](https://github.com/mendableai/firecrawl)
- **License**: MIT

## Use the Agent

### 1. Clone & Install Dependencies

<details>

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system. If you are trying to run Open Deep Research agent and require an input, you can either create your agent which communicates on the coral server or run and register the [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent) on the Coral Server.  


```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/firecrawl-coral-agent.git

# Navigate to the project directory:
cd firecrawl-coral-agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync

# Copy the client sse.py from utils to mcp package (Linux/ Mac)
cp -r utils/sse.py .venv/lib/python3.13/site-packages/mcp/client/sse.py

# OR Copy this for Windows
cp -r utils\sse.py .venv\Lib\site-packages\mcp\client\sse.py

```

</details>

### 2. Configure Environment Variables

<details>

Get the API Key:
[OpenAI](https://platform.openai.com/api-keys) ||
[Firecrawl](https://www.firecrawl.dev/app/api-keys)

```bash
# Create .env file in project root
cp -r .env_sample .env
```

Check if the .env file has correct URL for Coral Server and adjust the parameters accordingly.

</details>

### 3. Run Agent

<details>

```bash
# Run the agent using `uv`:
uv run python firecrawl_coral_agent.py
```

### 4. Example

<details>

```bash
# Input:
What is Model Context Protocol?

#Output:
The Model Context Protocol (MCP) is an innovative open-source standard designed to enhance the interaction between artificial intelligence (AI) models and external tools and data sources. Introduced by Anthropic in November 2024, MCP addresses a critical challenge in the AI space by enabling seamless integration among diverse applications, particularly large language models (LLMs). This protocol streamlines data sharing and context management, offering a cohesive framework that allows AI systems to access real-time information efficiently. By eliminating the need for custom integrations, MCP fosters a more dynamic and interconnected AI ecosystem, thus empowering developers to create responsive and context-aware applications.
```

</details>


## Creator Details
- **Name**: Suman Deb
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)

