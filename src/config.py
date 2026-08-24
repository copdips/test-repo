"""Application configuration loading."""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """Runtime configuration."""

    host: str
    port: int
    debug: bool


def load_config() -> Config:
    """Build a `Config` from environment variables."""
    return Config(
        host=os.environ.get("APP_HOST", "localhost"),
        port=int(os.environ.get("APP_PORT", "8000")),
        debug=os.environ.get("APP_DEBUG", "false") == "true",
    )
