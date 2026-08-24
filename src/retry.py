"""Retry helper."""

import time
from collections.abc import Callable


def retry[T](fn: Callable[[], T], attempts: int = 3) -> T:
    """Call `fn`, retrying up to `attempts` times on exception."""
    for i in range(attempts):
        try:
            return fn()
        except Exception:
            if i == attempts - 1:
                raise
            time.sleep(1)
    raise AssertionError("unreachable")
