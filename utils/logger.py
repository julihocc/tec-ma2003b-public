"""Centralized logging utilities for MA2003B course examples.

Usage pattern (see `.github/copilot-instructions.md`):

    from utils import setup_logger
    logger = setup_logger(__name__)
    logger.info("Analysis starting...")

Purpose:
- Provide consistent formatting across all educational scripts
- Avoid duplicate handlers when modules re-import in interactive sessions
- Default INFO level to keep notebooks/scripts readable

This file was (re)introduced after being absent in the current worktree so that
existing imports `from utils import setup_logger` resolve correctly (Pylance / runtime).
"""
from __future__ import annotations

import logging
import os
import sys
from typing import Optional

# Simple colored level names (ANSI) if terminal supports it
_COLOR_MAP = {
    "DEBUG": "\x1b[36m",   # Cyan
    "INFO": "\x1b[32m",    # Green
    "WARNING": "\x1b[33m", # Yellow
    "ERROR": "\x1b[31m",   # Red
    "CRITICAL": "\x1b[41m",  # Red background
}
_RESET = "\x1b[0m"

def _supports_color(stream) -> bool:
    return hasattr(stream, "isatty") and stream.isatty() and os.environ.get("NO_COLOR") is None

class _CourseFormatter(logging.Formatter):
    def __init__(self, use_color: bool) -> None:
        super().__init__("%(asctime)s | %(levelname)s | %(name)s | %(message)s", "%H:%M:%S")
        self.use_color = use_color

    def format(self, record: logging.LogRecord) -> str:  # type: ignore[override]
        original_levelname = record.levelname
        if self.use_color and original_levelname in _COLOR_MAP:
            record.levelname = f"{_COLOR_MAP[original_levelname]}{original_levelname}{_RESET}"
        try:
            return super().format(record)
        finally:
            record.levelname = original_levelname  # restore to avoid side-effects

def setup_logger(name: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
    """Return a configured logger.

    Parameters
    ----------
    name: module or logical component name (defaults to root or provided __name__)
    level: logging level (defaults to INFO)

    Behavior
    --------
    - Adds a single StreamHandler to stdout if not already present
    - Applies consistent formatter (with colors if supported)
    - Safe to call repeatedly; will not duplicate handlers
    """
    logger_name = name if name not in (None, "__main__") else "ma2003b"
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Avoid duplicated handlers across interactive reloads
    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setLevel(level)
        handler.setFormatter(_CourseFormatter(_supports_color(sys.stdout)))
        logger.addHandler(handler)

    # Propagate disabled to prevent double logging under root
    logger.propagate = False
    return logger

__all__ = ["setup_logger"]
