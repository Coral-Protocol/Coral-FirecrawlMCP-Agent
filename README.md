# Firecrawl agent

## Features
* Short-term memory
* Claiming for results and work done to earn money
* Working with Coral messages via [MCP Resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources)
which allows agents to instantly receive new messages addressed to them.
* Uses firecrawl MCP

## Developing with this
### Requirements
1. Python 3.13+
2. OpenAI API key or compatible API key (e.g. openrouter) 
3. Coral server running locally

### Running in devmode
[Devmode](https://docs.coralprotocol.org/guides/writing-agents#devmode) allows you to run an agent using your preferred tooling and it will connect to a yet to exist session, where the server will see devmode is enabled and create the session for you.
This is the recommended method of developing indvidual agents since it saves you from needing to manually create sessions to test out each iteration.
See the [docs](https://docs.coralprotocol.org/guides/writing-agents#devmode) for more info.

This template will load the local .env when in devmode, determined by CORAL_ORCHESTRATION_RUNTIME not being set (the coral server would set it outside of devmode)


## Support & Resources
Docs: [Coral Protocol Documentation](https://docs.coralprotocol.org/)
Community: [Coral Discord](https://discord.gg/MqcwYy6gxV)

