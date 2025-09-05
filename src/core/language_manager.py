"""
Language management for Git Account Manager Pro.
"""

import json
import os
from typing import Dict, Any, Optional

from ..config.constants import CONFIG_FILES, LANGUAGES, APP_SETTINGS
from ..config.translations import TRANSLATIONS


class LanguageManager:
    """Manages application language and translations."""
    
    def __init__(self):
        self.current_language = APP_SETTINGS['default_language']
        self.translations = TRANSLATIONS
        self.available_languages = LANGUAGES
    
    def load_language_config(self) -> Dict[str, Any]:
        """Load language configuration from file."""
        if not os.path.exists(CONFIG_FILES['language_config']):
            # Create default config
            language_config = {"language": self.current_language}
            self.save_language_config(language_config)
            return language_config
        
        try:
            with open(CONFIG_FILES['language_config'], 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            language_setting = config.get("language", self.current_language)
            self.current_language = language_setting
            
            return config
            
        except Exception as e:
            print(f"Error loading language config: {e}")
            self.current_language = APP_SETTINGS['default_language']
            return {"language": self.current_language}
    
    def save_language_config(self, config: Dict[str, Any]) -> None:
        """Save language configuration to file."""
        try:
            # Ensure data directory exists
            os.makedirs(os.path.dirname(CONFIG_FILES['language_config']), exist_ok=True)
            
            with open(CONFIG_FILES['language_config'], 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving language config: {e}")
    
    def set_language(self, language_code: str) -> None:
        """Set the current language."""
        if language_code in self.available_languages:
            self.current_language = language_code
            
            # Save language preference
            config = {"language": language_code}
            self.save_language_config(config)
            
            print(f"🌐 Language set to: {self.get_language_name(language_code)}")
        else:
            print(f"❌ Unsupported language: {language_code}")
    
    def get_current_language(self) -> str:
        """Get current language code."""
        return self.current_language
    
    def get_language_name(self, language_code: str = None) -> str:
        """Get language name for given code or current language."""
        if language_code is None:
            language_code = self.current_language
        
        return self.available_languages.get(language_code, {}).get('name', 'Unknown')
    
    def get_language_flag(self, language_code: str = None) -> str:
        """Get language flag emoji for given code or current language."""
        if language_code is None:
            language_code = self.current_language
        
        return self.available_languages.get(language_code, {}).get('flag', '🌐')
    
    def get_language_icon(self, language_code: str = None) -> str:
        """Get language icon emoji for given code or current language."""
        if language_code is None:
            language_code = self.current_language
        
        return self.available_languages.get(language_code, {}).get('icon', '🌐')
    
    def get_available_languages(self) -> Dict[str, Dict[str, str]]:
        """Get all available languages."""
        return self.available_languages
    
    def translate(self, key: str, language_code: str = None) -> str:
        """Get translation for a key in specified or current language."""
        if language_code is None:
            language_code = self.current_language
        
        # Get translation for the language
        language_translations = self.translations.get(language_code, {})
        translation = language_translations.get(key, key)
        
        # If translation not found, try English as fallback
        if translation == key and language_code != 'en':
            english_translations = self.translations.get('en', {})
            translation = english_translations.get(key, key)
        
        return translation
    
    def get_all_translations(self, language_code: str = None) -> Dict[str, str]:
        """Get all translations for a language."""
        if language_code is None:
            language_code = self.current_language
        
        return self.translations.get(language_code, {})
    
    def initialize(self) -> None:
        """Initialize language manager by loading configuration."""
        self.load_language_config()
