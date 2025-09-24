"""Utilities package exposing logging setup for course examples.

This package provides a single public helper:

    from utils import setup_logger

which returns a configured `logging.Logger` instance with a consistent
format used across all educational scripts. Having this module ensures
that Pylance and static analyzers can resolve the import `utils`.
"""
from .logger import setup_logger  # re-export for convenience

__all__ = ["setup_logger"]
