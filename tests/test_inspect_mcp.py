
import inspect
from mcp.server.fastmcp import FastMCP

def inspect_fastmcp():
    print(inspect.signature(FastMCP.run))
    print(inspect.getdoc(FastMCP.run))

if __name__ == "__main__":
    try:
        inspect_fastmcp()
    except Exception as e:
        print(f"Error: {e}")
