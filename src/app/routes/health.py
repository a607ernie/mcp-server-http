from mcp.server.fastmcp import FastMCP


def register_health_routes(mcp: FastMCP) -> None:
	@mcp.custom_route("/health", methods=["GET"])
	async def health_check(request):
		"""健康檢查端點"""
		from starlette.responses import JSONResponse

		return JSONResponse({"status": "healthy"})
