import pytest
from mcp.server.fastmcp import FastMCP

from src.app.tools.users import register_user_tools, get_all_users_data, get_user_info_data


def test_register_user_tools():
    """測試用戶工具註冊"""
    mcp = FastMCP("test")
    # 應該不拋出異常
    register_user_tools(mcp)


def test_get_all_users_data():
    """測試獲取所有用戶數據"""
    result = get_all_users_data()
    assert "小明" in result
    assert "小華" in result
    assert "小美" in result


@pytest.mark.parametrize("user_id,expected_contains", [
    ("1", "小明"),
    ("2", "小華"),
    ("3", "小美"),
])
def test_get_user_info_known_users(user_id, expected_contains):
    """測試已知用戶的信息"""
    result = get_user_info_data(user_id)
    assert expected_contains in result


def test_get_user_info_unknown_user():
    """測試未知用戶"""
    result = get_user_info_data("999")
    assert "找不到用戶。" in result
