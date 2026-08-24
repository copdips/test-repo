"""Greeting helpers."""


def greet(name: str) -> str:
    """Return a greeting for `name`."""
    return f"Hello, {name}"


def greet_all(names: list[str]) -> list[str]:
    """Return a greeting for each name in `names`."""
    return [greet(n) for n in names]
