"""
Configuration management module for Git Account Manager Pro.
Handles themes, settings, and application configuration.
"""

from .settings import ConfigManager, ThemeManager
from .constants import *

__all__ = ['ConfigManager', 'ThemeManager', 'THEMES', 'CONFIG_FILES']
