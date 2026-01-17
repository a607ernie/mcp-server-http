import pytest
from mcp.server.fastmcp import FastMCP

from src.app.routes.health import register_health_routes


def test_register_health_routes():
    """測試健康路由註冊"""
    mcp = FastMCP("test")
    # 應該不拋出異常
    register_health_routes(mcp)
