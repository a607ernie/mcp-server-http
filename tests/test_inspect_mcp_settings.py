
import inspect
from mcp.server.fastmcp import FastMCP

def inspect_fastmcp():
    mcp = FastMCP("test")
    settings = mcp.settings
    print(f"Settings dir: {dir(settings)}")
    if hasattr(settings, 'port'):
        print(f"Default Port: {settings.port}")
    else:
        print("Settings object has no 'port' attribute")
    
    if hasattr(settings, 'host'):
        print(f"Default Host: {settings.host}")

if __name__ == "__main__":
    try:
        inspect_fastmcp()
    except Exception as e:
        print(f"Error: {e}")
