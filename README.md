## [Firecrawl Coral Agent](https://github.com/Coral-Protocol/firecrawl-coral-agent.git)
The Firecrawl Coral Agent is an open-source agent designed for comprehensive web scraping, crawling, and data extraction tasks.

### Responsibility
The Firecrawl Coral Agent is an open-source agent designed for comprehensive web scraping, crawling, and data extraction tasks. It excels in structured data extraction and deep research by leveraging a multi-agent architecture to efficiently navigate, search, and analyze web content.


### Details
- **Framework**: LangChain
- **Tools used**: Firecrawl MCP Server Tools, Coral Server Tools
- **AI model**: OpenAI GPT-4o
- **Date added**: June 4, 2025
- **Reference**: [Firecrawl MCP Repo](https://github.com/mendableai/firecrawl)
- **License**: MIT

### Clone & Install Dependencies

1. Run [Coral Server](https://github.com/Coral-Protocol/coral-server)
<details>

This agent runs on Coral Server, follow the instrcutions below to run the server. In a new terminal clone the repository:


```bash
git clone https://github.com/Coral-Protocol/coral-server.git
```

Navigate to the project directory:
```bash
cd coral-server
```
Run the server
```bash
cd ./gradlew run
```
</details>

2. Run [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent)

<details>

If you are trying to run Open Deep Research agent and require an input, you can either create your agent which communicates on the coral server or run and register the Interface Agent on the Coral Server. In a new terminal clone the repository:


```bash
git clone https://github.com/Coral-Protocol/Coral-Interface-Agent.git
```
Navigate to the project directory:
```bash
cd Coral-Interface-Agent
```

Install `uv`:
```bash
pip install uv
```
Install dependencies from `pyproject.toml` using `uv`:
```bash
uv sync
```

Configure API Key
```bash
export OPENAI_API_KEY=
```

Run the agent using `uv`:
```bash
uv run python 0-langchain-interface.py
```

</details>

3. Agent Installation

<details>

Clone the repository:
```bash
git clone https://github.com/Coral-Protocol/firecrawl-coral-agent.git
```

Navigate to the project directory:
```bash
cd firecrawl-coral-agent
```

Install `uv`:
```bash
pip install uv
```

Install dependencies from `pyproject.toml` using `uv`:
```bash
uv sync
```

This command will read the `pyproject.toml` file and install all specified dependencies in a virtual environment managed by `uv`.

</details>

### Configure Environment Variables
Get the API Key:
[OpenAI](https://platform.openai.com/api-keys)
[Firecrawl](https://www.firecrawl.dev/app/api-keys)

Rename the sample environment file to `.env` and add the keys:
```bash
mv .env_sample .env
```
Check if the environment file has correct URL for Coral Server and adjust the parameters accordingly.

### Run Agent
Run the agent using `uv`:
```bash
uv run python firecrawl_coral_agent.py
```

### Example Output
```
The Model Context Protocol (MCP) is an innovative open-source standard designed to enhance the interaction between artificial intelligence (AI) models and external tools and data sources. Introduced by Anthropic in November 2024, MCP addresses a critical challenge in the AI space by enabling seamless integration among diverse applications, particularly large language models (LLMs). This protocol streamlines data sharing and context management, offering a cohesive framework that allows AI systems to access real-time information efficiently. By eliminating the need for custom integrations, MCP fosters a more dynamic and interconnected AI ecosystem, thus empowering developers to create responsive and context-aware applications.

```

### Creator Details
- **Name**: Suman Deb
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)

