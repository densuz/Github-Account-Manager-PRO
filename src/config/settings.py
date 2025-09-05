"""
Settings and theme management for Git Account Manager Pro.
"""

import json
import os
import tkinter as tk
from typing import Dict, Any, Optional

from .constants import THEMES, CONFIG_FILES, APP_SETTINGS


class ThemeManager:
    """Manages application themes and theme switching."""
    
    def __init__(self):
        self.current_theme = APP_SETTINGS['default_theme']
        self.theme_colors = THEMES[self.current_theme]
    
    def detect_system_theme(self) -> str:
        """Detect system theme preference."""
        try:
            # Check if system is in dark mode (Windows 10/11)
            try:
                import winreg
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER, 
                    r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
                )
                value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
                winreg.CloseKey(key)
                return "light" if value == 1 else "dark"
            except:
                # Fallback: check tkinter's default colors
                root = tk.Tk()
                root.withdraw()  # Hide the window
                bg_color = root.cget('bg')
                root.destroy()
                # If background is light, assume light theme
                if bg_color in ['#f0f0f0', '#ffffff', 'SystemWindow']:
                    return "light"
                else:
                    return "dark"
        except:
            return "dark"  # Default fallback
    
    def load_theme_config(self) -> Dict[str, Any]:
        """Load theme configuration from file."""
        if not os.path.exists(CONFIG_FILES['theme_config']):
            # Create default config
            theme_config = {"theme": "system"}
            self.save_theme_config(theme_config)
            return theme_config
        
        try:
            with open(CONFIG_FILES['theme_config'], 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            theme_setting = config.get("theme", "system")
            
            if theme_setting == "system":
                self.current_theme = self.detect_system_theme()
            else:
                self.current_theme = theme_setting
            
            self.theme_colors = THEMES[self.current_theme]
            return config
            
        except Exception as e:
            print(f"Error loading theme config: {e}")
            self.current_theme = "dark"
            self.theme_colors = THEMES["dark"]
            return {"theme": "dark"}
    
    def save_theme_config(self, config: Dict[str, Any]) -> None:
        """Save theme configuration to file."""
        try:
            with open(CONFIG_FILES['theme_config'], 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            print(f"Error saving theme config: {e}")
    
    def apply_theme(self, theme_name: str) -> None:
        """Apply theme and update global variables."""
        if theme_name == "system":
            self.current_theme = self.detect_system_theme()
        else:
            self.current_theme = theme_name
        
        self.theme_colors = THEMES[self.current_theme]
        
        # Save theme preference
        config = {"theme": theme_name}
        self.save_theme_config(config)
        
        print(f"🎨 Theme applied: {self.current_theme}")
    
    def get_theme_colors(self) -> Dict[str, str]:
        """Get current theme colors."""
        return self.theme_colors
    
    def get_current_theme(self) -> str:
        """Get current theme name."""
        return self.current_theme


class ConfigManager:
    """Manages application configuration and settings."""
    
    def __init__(self):
        self.theme_manager = ThemeManager()
        self.settings = APP_SETTINGS.copy()
    
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        return self.settings.get(key, default)
    
    def set_setting(self, key: str, value: Any) -> None:
        """Set a configuration setting."""
        self.settings[key] = value
    
    def get_theme_manager(self) -> ThemeManager:
        """Get the theme manager instance."""
        return self.theme_manager
    
    def initialize(self) -> None:
        """Initialize configuration by loading theme settings."""
        self.theme_manager.load_theme_config()
