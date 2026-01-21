import pytest
from mcp.server.fastmcp import FastMCP

from src.app.tools.weather import register_weather_tools, get_weather_data


def test_register_weather_tools():
    """測試天氣工具註冊"""
    mcp = FastMCP("test")
    # 應該不拋出異常
    register_weather_tools(mcp)


@pytest.mark.parametrize("city,expected", [
    ("New York", "晴天, -45°C"),
    ("Los Angeles", "多雲, -55°C"),
    ("Chicago", "雨天, 65°C"),
    ("Taipei", "晴天, 87°C"),
])
def test_get_weather_known_cities(city, expected):
    """測試已知城市的天气"""
    result = get_weather_data(city)
    assert expected in result


def test_get_weather_unknown_city():
    """測試未知城市的天气"""
    result = get_weather_data("Unknown City")
    assert "此城市的天氣資料不可用。" in result
