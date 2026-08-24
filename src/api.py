"""HTTP API routes."""

from src.auth import User, authenticate


def get_user_route(token: str) -> tuple[int, dict[str, str | int]]:
    """Return an HTTP status and body for the current-user endpoint."""
    user: User | None = authenticate(token)
    if user is None:
        return 401, {"error": "unauthorized"}
    return 200, {"id": user.id, "name": user.name}
