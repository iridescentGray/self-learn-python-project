from fastmcp import FastMCP

mcp = FastMCP("My MCP Server", port=9000)

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
