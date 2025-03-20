from mcp.server.fastmcp import FastMCP
import math


mcp = FastMCP("hello ji")


# define whatever functions you want to use in the calculator

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    return a / b

@mcp.tool()
def power(a: int, b: int) -> int:
    return math.pow(a, b)

@mcp.tool()
def sqrt(a: int) -> float:
    return math.sqrt(a)

@mcp.tool()
def factorial(a: int) -> int:
    return math.factorial(a)

@mcp.tool()
def sin(a: int) -> float:
    return math.sin(a)

@mcp.tool()
def cos(a: int) -> float:
    return math.cos(a)

@mcp.tool()
def tan(a: int) -> float:
    return math.tan(a)

@mcp.tool()
def log(a: int) -> float:
    return math.log(a)

@mcp.resource("greeting://{name}")
def greet(name: str) -> str:
    return f"Hello {name}!"


if __name__ == "__main__":
    mcp.run(transport="stdio")