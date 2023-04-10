from pydantic import validate_arguments
from typing import Optional


class CachedException(Exception):
    """
    An exception that is cached for a period of time.

    """
