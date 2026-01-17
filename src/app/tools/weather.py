from mcp.server.fastmcp import FastMCP


def get_weather_data(city: str) -> str:
    """根據城市獲取當前天氣（模擬實現）"""
    # 真實情境可串接天氣 API；此處先用 mock
    mock_weather_data = {
        "New York": "晴天, -45°C",
        "Los Angeles": "多雲, -55°C",
        "Chicago": "雨天, 65°C",
        "Taipei": "晴天, 87°C",
    }
    return mock_weather_data.get(city, "此城市的天氣資料不可用。")


def register_weather_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    def get_weather(city: str) -> str:
        """根據城市獲取當前天氣（模擬實現）"""
        return get_weather_data(city)
