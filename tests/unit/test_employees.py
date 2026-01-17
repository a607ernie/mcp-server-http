import pytest
from mcp.server.fastmcp import FastMCP

from src.app.tools.employees import register_employee_tools, get_employee_info_data


def test_register_employee_tools():
    """測試員工工具註冊"""
    mcp = FastMCP("test")
    # 應該不拋出異常
    register_employee_tools(mcp)


@pytest.mark.parametrize("employee_id,expected_contains", [
    ("EMP001", "王小明"),
    ("EMP002", "李小華"),
    ("EMP003", "陳小美"),
    ("EMP004", "林小智"),
])
def test_get_employee_info_known_employees(employee_id, expected_contains):
    """測試已知員工的信息"""
    result = get_employee_info_data(employee_id)
    assert expected_contains in result


def test_get_employee_info_unknown_employee():
    """測試未知員工"""
    result = get_employee_info_data("EMP999")
    assert "找不到員工。" in result