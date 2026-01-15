
# MCP Demo Server

A minimal **Model Context Protocol (MCP)** server using **Streamable HTTP**,
ready to deploy on **Render**.

- MCP path: `/mcp`
- Transport: `streamable-http`
- Tool: `get_weather(city: str) -> str`

## Local run

```bash
pip install -r requirements.txt
export PORT=8000
python -m src.server
