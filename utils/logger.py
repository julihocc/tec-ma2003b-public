"""Simple logger setup utility.

Provides a setup_logger function that configures a logger with a StreamHandler
and optional FileHandler. This keeps logging configuration centralized for
scripts and tests.
"""

from __future__ import annotations

import logging
from typing import Optional


def setup_logger(
    name: Optional[str] = None,
    level: int = logging.INFO,
    *,
    logfile: Optional[str] = None,
    fmt: Optional[str] = None,
) -> logging.Logger:
    """Create and configure a logger.

    Args:
        name: logger name (None gives root logger).
        level: logging level (e.g., logging.DEBUG).
        logfile: optional path to a logfile. If provided, a FileHandler is added.
        fmt: optional logging format string. A sensible default is used otherwise.

    Returns:
        Configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # If logger already has handlers, assume it's configured and return it after setting level
    if logger.handlers:
        logger.setLevel(level)
        return logger

    if fmt is None:
        fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    formatter = logging.Formatter(fmt)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if logfile:
        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Avoid message duplication when root logger is also configured
    logger.propagate = False

    return logger
