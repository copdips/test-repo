"""Authentication primitives."""

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    """An authenticated user."""

    id: int
    name: str


def authenticate(token: str) -> User | None:
    """Resolve `token` to a `User`, or None when the token is unknown."""
    if not token.startswith("tok-"):
        return None
    return User(id=123, name="foo")
