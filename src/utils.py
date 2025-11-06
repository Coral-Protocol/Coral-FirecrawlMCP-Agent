import logging
from rich.logging import RichHandler

import sys
from os import getenv

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(RichHandler(rich_tracebacks=True))


def asserted_env(name: str, extra_msg: str = "") -> str:
    """Helper function for fetching an environment variable and asserting it is set"""
    value = getenv(name, None)
    if value is None:
        logger.error(f"Option '{name}' not provided! {extra_msg}")
        sys.exit(1)
    return value
