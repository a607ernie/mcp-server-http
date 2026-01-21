
# src/server.py
import os
from datetime import datetime
from mcp.server.fastmcp import FastMCP

# 建立 MCP 伺服器
mcp = FastMCP("mcp_demo_server")
mcp.settings.host = "0.0.0.0"
mcp.settings.port = int(os.environ.get("PORT", 8000))

@mcp.tool()
def get_weather(city: str) -> str:
    """根據城市獲取當前天氣（模擬實現）"""
    # 真實情境可串接天氣 API；此處先用 mock
    mock_weather_data = {
        "New York": "晴天, -45°C",
        "Los Angeles": "多雲, -55°C",
        "Chicago": "雨天, 65°C",
        "Taipei": "晴天, 87°C",
    }
    return mock_weather_data.get(city, "此城市的天氣資料不可用。")



@mcp.tool()
def get_user_info(user_id: str) -> str:
    """根據用戶 ID 獲取用戶資訊（模擬實現）"""
    mock_user_data = {
        "1": "姓名: 小明, 年齡: 30, 電子郵件: xiaoming@example.com",
        "2": "姓名: 小華, 年齡: 25, 電子郵件: xiaohua@example.com",
        "3": "姓名: 小美, 年齡: 35, 電子郵件: xiaomei@example.com",
    }
    return mock_user_data.get(user_id, "找不到用戶。")


@mcp.tool()
def search_products(query: str) -> str:
    """根據查詢搜索產品（模擬實現）"""
    mock_products = {
        "筆電": "找到: Dell XPS 13 - $999, Lenovo ThinkPad - $899",
        "手機": "找到: iPhone 15 - $1199, Samsung Galaxy S24 - $1099",
        "書籍": "找到: Python 程式設計入門 - $29, 乾淨程式碼 - $39",
    }
    return mock_products.get(query.lower(), f"找不到 '{query}' 的產品。")


@mcp.tool()
def get_latest_news(category: str) -> str:
    """根據類別獲取最新新聞（模擬實現）"""
    mock_news = {
        "科技": "最新: 2026年AI進展, 新量子電腦突破。",
        "體育": "最新: NBA總決賽更新, 足球世界盃準備。",
        "政治": "最新: 全球氣候高峰會, 選舉結果。",
    }
    return mock_news.get(category.lower(), f"沒有 '{category}' 類別的新聞。")


@mcp.tool()
def calculate(expression: str) -> str:
    """簡單計算器用於基本算術（模擬實現）"""
    try:
        # 使用 eval 進行簡單計算，注意安全性（在生產環境中避免）
        result = eval(expression)
        return f"結果: {result}"
    except Exception as e:
        return f"錯誤: {str(e)}"


@mcp.tool()
def get_employee_info(employee_id: str) -> str:
    """根據員工 ID 獲取員工資訊（模擬實現）"""
    mock_employee_data = {
        "EMP001": "姓名: 王小明, 工號: EMP001, 廠區: 台北廠, 部門: 工程部, 可休假餘額: 15 天",
        "EMP002": "姓名: 李小華, 工號: EMP002, 廠區: 高雄廠, 部門: 銷售部, 可休假餘額: 10 天",
        "EMP003": "姓名: 陳小美, 工號: EMP003, 廠區: 台北廠, 部門: 人事部, 可休假餘額: 20 天",
        "EMP004": "姓名: 林小智, 工號: EMP004, 廠區: 台中廠, 部門: 財務部, 可休假餘額: 12 天",
    }
    return mock_employee_data.get(employee_id, "找不到員工。")


@mcp.tool()
def get_current_time() -> str:
    """獲取當前時間"""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    # 以 Streamable HTTP 啟動，Render 會以環境變數 PORT 指派埠號
    # 路徑固定為 /mcp，方便 MCP Inspector 或客戶端連線
    mcp.run(transport="streamable-http")
