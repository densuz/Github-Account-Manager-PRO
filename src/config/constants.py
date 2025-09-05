"""
Constants and configuration values for Git Account Manager Pro.
"""

# File paths - Secure data directory
CONFIG_FILES = {
    'accounts': 'data/accounts.json',
    'current_profile': 'data/.git_current_profile',
    'theme_config': 'data/theme_config.json'
}

# Theme definitions
THEMES = {
    "dark": {
        "bg_primary": "#1e1e2e",
        "bg_secondary": "#313244", 
        "bg_tertiary": "#45475a",
        "text_primary": "#cdd6f4",
        "text_secondary": "#a6adc8",
        "text_muted": "#6c7086",
        "accent_blue": "#89b4fa",
        "accent_green": "#a6e3a1",
        "accent_yellow": "#f9e2af",
        "accent_red": "#f38ba8",
        "accent_purple": "#cba6f7",
        "border": "#313244",
        "hover_blue": "#74c0fc",
        "hover_green": "#94d3a2",
        "hover_yellow": "#f5d76e",
        "hover_red": "#f06292"
    },
    "light": {
        "bg_primary": "#ffffff",
        "bg_secondary": "#f8f9fa",
        "bg_tertiary": "#e9ecef",
        "text_primary": "#212529",
        "text_secondary": "#495057",
        "text_muted": "#6c757d",
        "accent_blue": "#0d6efd",
        "accent_green": "#198754",
        "accent_yellow": "#ffc107",
        "accent_red": "#dc3545",
        "accent_purple": "#6f42c1",
        "border": "#dee2e6",
        "hover_blue": "#0b5ed7",
        "hover_green": "#157347",
        "hover_yellow": "#ffca2c",
        "hover_red": "#bb2d3b"
    }
}

# Application settings
APP_SETTINGS = {
    'default_theme': 'dark',
    'window_size': '650x600',
    'min_window_size': (600, 500),
    'command_timeout': 30
}

# Git configuration defaults
GIT_DEFAULTS = {
    'init_default_branch': 'main',
    'pull_rebase': False,
    'push_default': 'simple',
    'credential_helper': 'store'
}
