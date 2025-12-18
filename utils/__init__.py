"""
Utilities Module for Omega Universal OS
Provides shared utilities, logging configuration, and configuration handling.
"""

from .logger import setup_logging, get_logger
from .config import Config, load_config

__all__ = ['setup_logging', 'get_logger', 'Config', 'load_config']
