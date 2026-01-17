from mcp.server.fastmcp import FastMCP


def get_all_users_data() -> str:
    """獲取所有用戶資訊（模擬實現）"""
    return (
        "用戶列表:\n"
        "1. 小明, 年齡: 30, 電子郵件: xiaoming@example.com\n"
        "2. 小華, 年齡: 25, 電子郵件: xiaohua@example.com\n"
        "3. 小美, 年齡: 35, 電子郵件: xiaomei@example.com\n"
    )


def get_user_info_data(user_id: str) -> str:
    """根據用戶 ID 獲取用戶資訊（模擬實現）"""
    mock_user_data = {
        "1": "姓名: 小明, 年齡: 30, 電子郵件: xiaoming@example.com",
        "2": "姓名: 小華, 年齡: 25, 電子郵件: xiaohua@example.com",
        "3": "姓名: 小美, 年齡: 35, 電子郵件: xiaomei@example.com",
    }
    return mock_user_data.get(user_id, "找不到用戶。")


def register_user_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    def get_all_users() -> str:
        """獲取所有用戶資訊（模擬實現）"""
        return get_all_users_data()

    @mcp.tool()
    def get_user_info(user_id: str) -> str:
        """根據用戶 ID 獲取用戶資訊（模擬實現）"""
        return get_user_info_data(user_id)
