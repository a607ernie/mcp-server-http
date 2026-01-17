
# src/server.py
from mcp.server.fastmcp import FastMCP

from app.routes.health import register_health_routes
from app.tools.employees import register_employee_tools
from app.tools.products import register_product_tools
from app.tools.users import register_user_tools
from app.tools.weather import register_weather_tools
from settings import HOST, MCP_NAME, PORT, TRANSPORT_SECURITY

# 建立 MCP 伺服器
mcp = FastMCP(
    MCP_NAME,
    transport_security=TRANSPORT_SECURITY,
)
mcp.settings.host = HOST
mcp.settings.port = PORT

# 註冊路由與工具
register_health_routes(mcp)
register_weather_tools(mcp)
register_user_tools(mcp)
register_product_tools(mcp)
register_employee_tools(mcp)

if __name__ == "__main__":
    # 以 Streamable HTTP 啟動，Render 會以環境變數 PORT 指派埠號
    # 路徑固定為 /mcp，方便 MCP Inspector 或客戶端連線
    mcp.run(transport="streamable-http")
