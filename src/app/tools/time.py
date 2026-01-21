from datetime import datetime
from mcp.server.fastmcp import FastMCP

def get_current_time() -> str:
    """獲取當前時間"""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def register_time_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    def get_current_time_tool() -> str:
        """獲取當前時間"""
        return get_current_time()