"""Greeting helpers."""


def greet(name: str) -> str:
    """Return a greeting for `name`."""
    return "Hello, " + name


def greet_all(names: list[str]) -> list[str]:
    """Return a greeting for each name in `names`."""
    result = []
    for n in names:
        result.append(greet(n))
    return result
