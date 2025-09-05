"""
File management utilities for Git Account Manager Pro.
"""

import json
import os
from typing import Dict, Any, Optional

from ..config.constants import CONFIG_FILES


class FileManager:
    """Handles file operations for configuration and data storage."""
    
    def __init__(self):
        self.config_files = CONFIG_FILES
    
    def load_json_file(self, file_path: str, default: Any = None) -> Any:
        """
        Load JSON data from file.
        
        Args:
            file_path: Path to JSON file
            default: Default value if file doesn't exist or fails to load
            
        Returns:
            Loaded JSON data or default value
        """
        # Ensure data directory exists
        self.ensure_config_directory()
        
        if not os.path.exists(file_path):
            return default
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return default
    
    def save_json_file(self, file_path: str, data: Any) -> bool:
        """
        Save data to JSON file.
        
        Args:
            file_path: Path to save file
            data: Data to save
            
        Returns:
            True if successful, False otherwise
        """
        # Ensure data directory exists
        self.ensure_config_directory()
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving {file_path}: {e}")
            return False
    
    def load_accounts(self) -> Dict[str, Any]:
        """
        Load accounts from configuration file.
        
        Returns:
            Dictionary of accounts
        """
        return self.load_json_file(self.config_files['accounts'], {})
    
    def save_accounts(self, accounts: Dict[str, Any]) -> bool:
        """
        Save accounts to configuration file.
        
        Args:
            accounts: Dictionary of accounts to save
            
        Returns:
            True if successful, False otherwise
        """
        return self.save_json_file(self.config_files['accounts'], accounts)
    
    def get_current_profile(self) -> Optional[str]:
        """
        Get current active profile from file.
        
        Returns:
            Current profile key or None if not found
        """
        try:
            if os.path.exists(self.config_files['current_profile']):
                with open(self.config_files['current_profile'], 'r', encoding='utf-8') as f:
                    return f.read().strip()
        except Exception as e:
            print(f"Error reading current profile: {e}")
        return None
    
    def save_current_profile(self, profile_key: str) -> bool:
        """
        Save current active profile to file.
        
        Args:
            profile_key: Key of the profile to set as current
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(self.config_files['current_profile'], 'w', encoding='utf-8') as f:
                f.write(profile_key)
            return True
        except Exception as e:
            print(f"Error saving current profile: {e}")
            return False
    
    def remove_current_profile(self) -> bool:
        """
        Remove current profile file.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if os.path.exists(self.config_files['current_profile']):
                os.remove(self.config_files['current_profile'])
            return True
        except Exception as e:
            print(f"Error removing current profile: {e}")
            return False
    
    def ensure_config_directory(self) -> None:
        """Ensure configuration directory exists."""
        import os
        # Create data directory if it doesn't exist
        data_dir = "data"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir, exist_ok=True)
            print(f"✅ Created secure data directory: {data_dir}")
