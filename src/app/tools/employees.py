from mcp.server.fastmcp import FastMCP


def get_employee_info_data(employee_id: str) -> str:
    """根據員工 ID 獲取員工資訊（模擬實現）"""
    mock_employee_data = {
        "EMP001": "姓名: 王小明, 工號: EMP001, 廠區: 台北廠, 部門: 工程部, 可休假餘額: 15 天",
        "EMP002": "姓名: 李小華, 工號: EMP002, 廠區: 高雄廠, 部門: 銷售部, 可休假餘額: 10 天",
        "EMP003": "姓名: 陳小美, 工號: EMP003, 廠區: 台北廠, 部門: 人事部, 可休假餘額: 20 天",
        "EMP004": "姓名: 林小智, 工號: EMP004, 廠區: 台中廠, 部門: 財務部, 可休假餘額: 12 天",
    }
    return mock_employee_data.get(employee_id, "找不到員工。")


def register_employee_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    def get_employee_info(employee_id: str) -> str:
        """根據員工 ID 獲取員工資訊（模擬實現）"""
        return get_employee_info_data(employee_id)
