import pytest
from mcp.server.fastmcp import FastMCP

from src.app.tools.products import register_product_tools, search_products_data, get_latest_news_data, calculate_data


def test_register_product_tools():
    """測試產品工具註冊"""
    mcp = FastMCP("test")
    # 應該不拋出異常
    register_product_tools(mcp)


@pytest.mark.parametrize("query,expected_contains", [
    ("筆電", "Dell XPS 13"),
    ("手機", "iPhone 15"),
    ("書籍", "Python 程式設計入門"),
])
def test_search_products_known_queries(query, expected_contains):
    """測試已知查詢的產品搜索"""
    result = search_products_data(query)
    assert expected_contains in result


def test_search_products_unknown_query():
    """測試未知查詢的產品搜索"""
    result = search_products_data("未知產品")
    assert "找不到 '未知產品' 的產品。" in result


@pytest.mark.parametrize("category,expected_contains", [
    ("科技", "AI進展"),
    ("體育", "NBA總決賽"),
    ("政治", "全球氣候高峰會"),
])
def test_get_latest_news_known_categories(category, expected_contains):
    """測試已知類別的新聞"""
    result = get_latest_news_data(category)
    assert expected_contains in result


def test_get_latest_news_unknown_category():
    """測試未知類別的新聞"""
    result = get_latest_news_data("未知類別")
    assert "沒有 '未知類別' 類別的新聞。" in result


@pytest.mark.parametrize("expression,expected", [
    ("2 + 3", "結果: 5"),
    ("10 * 2", "結果: 20"),
    ("8 / 2", "結果: 4.0"),
])
def test_calculate_valid_expressions(expression, expected):
    """測試有效的計算表達式"""
    result = calculate_data(expression)
    assert result == expected


def test_calculate_invalid_expression():
    """測試無效的計算表達式"""
    result = calculate_data("invalid expression")
    assert "錯誤:" in result