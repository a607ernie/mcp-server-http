from mcp.server.fastmcp import FastMCP


def search_products_data(query: str) -> str:
    """根據查詢搜索產品（模擬實現）"""
    mock_products = {
        "筆電": "找到: Dell XPS 13 - $999, Lenovo ThinkPad - $899",
        "手機": "找到: iPhone 15 - $1199, Samsung Galaxy S24 - $1099",
        "書籍": "找到: Python 程式設計入門 - $29, 乾淨程式碼 - $39",
    }
    return mock_products.get(query.lower(), f"找不到 '{query}' 的產品。")


def get_latest_news_data(category: str) -> str:
    """根據類別獲取最新新聞（模擬實現）"""
    mock_news = {
        "科技": "最新: 2026年AI進展, 新量子電腦突破。",
        "體育": "最新: NBA總決賽更新, 足球世界盃準備。",
        "政治": "最新: 全球氣候高峰會, 選舉結果。",
    }
    return mock_news.get(category.lower(), f"沒有 '{category}' 類別的新聞。")


def calculate_data(expression: str) -> str:
    """簡單計算器用於基本算術（模擬實現）"""
    try:
        # 使用 eval 進行簡單計算，注意安全性（在生產環境中避免）
        result = eval(expression)
        return f"結果: {result}"
    except Exception as e:
        return f"錯誤: {str(e)}"


def register_product_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    def search_products(query: str) -> str:
        """根據查詢搜索產品（模擬實現）"""
        return search_products_data(query)

    @mcp.tool()
    def get_latest_news(category: str) -> str:
        """根據類別獲取最新新聞（模擬實現）"""
        return get_latest_news_data(category)

    @mcp.tool()
    def calculate(expression: str) -> str:
        """簡單計算器用於基本算術（模擬實現）"""
        return calculate_data(expression)
