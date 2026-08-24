"""Client-side rendering of API responses."""

from src.api import get_user_route


def render_profile(token: str) -> str:
    """Render the profile page body for `token`."""
    status, payload = get_user_route(token)
    if status != 200:
        return "Please sign in."
    return f"Signed in as {payload['name']}"
