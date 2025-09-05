"""
Git operations manager for Git Account Manager Pro.
"""

import os
from typing import Dict, Any, Optional

from ..utils.command_runner import CommandRunner
from ..utils.file_manager import FileManager
from ..config.constants import GIT_DEFAULTS


class GitManager:
    """Manages Git configuration and operations."""
    
    def __init__(self):
        self.command_runner = CommandRunner()
        self.file_manager = FileManager()
    
    def check_git_availability(self) -> bool:
        """
        Check if Git is installed and available.
        
        Returns:
            True if Git is available, False otherwise
        """
        return self.command_runner.check_git_installed()
    
    def get_current_git_config(self) -> Dict[str, str]:
        """
        Get current Git configuration.
        
        Returns:
            Dictionary with current Git config values
        """
        config = {}
        try:
            config['name'] = self.command_runner.run_git_command('config --global user.name')
        except:
            config['name'] = ""
        
        try:
            config['email'] = self.command_runner.run_git_command('config --global user.email')
        except:
            config['email'] = ""
        
        try:
            config['username'] = self.command_runner.run_git_command('config --global github.user')
        except:
            config['username'] = ""
        
        return config
    
    def clean_old_url_rewrites(self) -> None:
        """Clean old URL rewrites from git config."""
        try:
            # Get all URL rewrites
            result = self.command_runner.run_git_command('config --global --get-regexp url\\..*\\.insteadOf')
            if result:
                lines = result.split('\n')
                for line in lines:
                    if 'github.com' in line:
                        # Extract the key and remove it
                        key = line.split(' ')[0]
                        try:
                            self.command_runner.run_git_command(f'config --global --unset "{key}"')
                            print(f"Cleaned old URL rewrite: {key}")
                        except:
                            pass
        except:
            pass  # Ignore errors
    
    def setup_credentials(self, username: str, token: str) -> None:
        """
        Setup Git credentials for automatic authentication.
        
        Args:
            username: GitHub username
            token: GitHub personal access token
        """
        try:
            # Set URL rewrite untuk menggunakan token
            self.command_runner.run_git_command(
                f'config --global url."https://{username}:{token}@github.com/".insteadOf "https://github.com/"'
            )
            
            # Simpan kredensial ke file .git-credentials
            home_dir = os.path.expanduser('~')
            credentials_file = os.path.join(home_dir, '.git-credentials')
            
            # Baca kredensial yang ada
            existing_credentials = []
            if os.path.exists(credentials_file):
                try:
                    with open(credentials_file, 'r', encoding='utf-8') as f:
                        existing_credentials = [line.strip() for line in f.readlines() if line.strip()]
                except Exception as e:
                    print(f"Warning: Could not read existing credentials: {e}")
                    existing_credentials = []
            
            # Hapus kredensial github.com yang lama
            existing_credentials = [cred for cred in existing_credentials if 'github.com' not in cred]
            
            # Tambah kredensial baru
            new_credential = f"https://{username}:{token}@github.com"
            existing_credentials.append(new_credential)
            
            # Simpan kembali ke file
            try:
                with open(credentials_file, 'w', encoding='utf-8') as f:
                    for cred in existing_credentials:
                        f.write(cred + '\n')
                print(f"✅ Credentials saved to {credentials_file}")
            except Exception as e:
                print(f"Warning: Could not save credentials: {e}")
                
        except Exception as e:
            print(f"Warning: Could not set up token authentication: {e}")
    
    def configure_git_account(self, account_data: Dict[str, Any]) -> None:
        """
        Configure Git with account information.
        
        Args:
            account_data: Dictionary containing account information
        """
        try:
            # 1. Set basic Git configuration
            self.command_runner.run_git_command(f'config --global user.name "{account_data["name"]}"')
            self.command_runner.run_git_command(f'config --global user.email "{account_data["email"]}"')
            
            # 2. Set GitHub username jika ada
            if "username" in account_data and account_data["username"]:
                self.command_runner.run_git_command(f'config --global github.user "{account_data["username"]}"')
            
            # 3. Configure credential helper untuk otomatis login
            self.command_runner.run_git_command(f'config --global credential.helper {GIT_DEFAULTS["credential_helper"]}')
            
            # 4. Set URL rewrite untuk GitHub (menggunakan token otomatis)
            if "token" in account_data and account_data["token"]:
                # Clean old URL rewrites
                self.clean_old_url_rewrites()
                
                # Setup credentials
                username = account_data.get('username', account_data['email'])
                self.setup_credentials(username, account_data["token"])
            
            # 5. Set additional Git configurations untuk kemudahan
            self.command_runner.run_git_command(f'config --global init.defaultBranch {GIT_DEFAULTS["init_default_branch"]}')
            self.command_runner.run_git_command(f'config --global pull.rebase {str(GIT_DEFAULTS["pull_rebase"]).lower()}')
            self.command_runner.run_git_command(f'config --global push.default {GIT_DEFAULTS["push_default"]}')
            
        except Exception as e:
            raise Exception(f"Failed to configure Git account: {str(e)}")
    
    def sync_current_profile(self) -> Optional[str]:
        """
        Sync current profile file with actual git configuration.
        
        Returns:
            Current profile key if found, None otherwise
        """
        try:
            # Get current git config
            current_config = self.get_current_git_config()
            
            # Find matching account
            accounts = self.file_manager.load_accounts()
            for key, data in accounts.items():
                if (data.get('name') == current_config['name'] and 
                    data.get('email') == current_config['email']):
                    # Update current profile file
                    self.file_manager.save_current_profile(key)
                    return key
            
            # If no match found, clear current profile
            self.file_manager.remove_current_profile()
            return None
            
        except Exception as e:
            print(f"Error syncing current profile: {e}")
            # Try to read from file as fallback
            return self.file_manager.get_current_profile()
    
    def switch_to_account(self, account_key: str, account_data: Dict[str, Any]) -> None:
        """
        Switch to a specific Git account.
        
        Args:
            account_key: Key of the account to switch to
            account_data: Account data dictionary
        """
        try:
            print(f"🔄 Switching to account: {account_key}")
            
            # Configure Git with account data
            self.configure_git_account(account_data)
            
            # Save current profile
            self.file_manager.save_current_profile(account_key)
            
            print(f"✅ Successfully switched to {account_key}")
            
        except Exception as e:
            raise Exception(f"Failed to switch account: {str(e)}")
