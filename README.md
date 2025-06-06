## [Firecrawl Coral Agent](https://github.com/Coral-Protocol/firecrawl-coral-agent.git)
The Firecrawl Coral Agent is an open-source agent designed for comprehensive web scraping, crawling, and data extraction tasks.

### Responsibility
The Firecrawl Coral Agent is an open-source agent designed for comprehensive web scraping, crawling, and data extraction tasks. It excels in structured data extraction and deep research by leveraging a multi-agent architecture to efficiently navigate, search, and analyze web content.


### Details
- **Framework**: LangChain
- **Tools used**: Firecrawl MCP Server Tools, Coral Server Tools
- **AI model**: OpenAI GPT-4o
- **Date added**: June 4, 2025
- **License**: MIT

### Clone & Install Dependencies
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
(Sample too big to post, check temp folder)
```

### Creator Details
- **Name**: Suman
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)
- **Link**: [Firecrawl MCP GitHub](https://github.com/mendableai/firecrawl)
