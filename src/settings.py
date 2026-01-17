import os
from mcp.server.transport_security import TransportSecuritySettings

MCP_NAME = "mcp-server-http"
HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8741))
TRANSPORT_SECURITY = TransportSecuritySettings(
	enable_dns_rebinding_protection=False,
)
