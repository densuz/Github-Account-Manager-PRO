"""
Account management for Git Account Manager Pro.
"""

from typing import Dict, Any, List, Tuple, Optional

from ..utils.file_manager import FileManager
from ..utils.validators import AccountValidator


class AccountManager:
    """Manages Git accounts and their operations."""
    
    def __init__(self):
        self.file_manager = FileManager()
        self.validator = AccountValidator()
    
    def load_accounts(self) -> Dict[str, Any]:
        """
        Load all accounts from storage.
        
        Returns:
            Dictionary of accounts
        """
        return self.file_manager.load_accounts()
    
    def save_accounts(self, accounts: Dict[str, Any]) -> bool:
        """
        Save accounts to storage.
        
        Args:
            accounts: Dictionary of accounts to save
            
        Returns:
            True if successful, False otherwise
        """
        return self.file_manager.save_accounts(accounts)
    
    def get_account(self, account_key: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific account by key.
        
        Args:
            account_key: Key of the account to retrieve
            
        Returns:
            Account data if found, None otherwise
        """
        accounts = self.load_accounts()
        return accounts.get(account_key)
    
    def add_account(self, account_data: Dict[str, Any]) -> Tuple[bool, str, Optional[str]]:
        """
        Add a new account.
        
        Args:
            account_data: Account data to add
            
        Returns:
            Tuple of (success, message, account_key)
        """
        # Validate account data
        is_valid, errors = self.validator.validate_account_data(account_data)
        if not is_valid:
            return False, f"Validation errors: {', '.join(errors)}", None
        
        accounts = self.load_accounts()
        
        # Generate account key
        account_key = self.validator.sanitize_account_key(account_data['name'])
        
        # Handle duplicate keys
        counter = 1
        original_key = account_key
        while account_key in accounts:
            account_key = f"{original_key}{counter}"
            counter += 1
        
        # Check for duplicate email
        for existing_key, existing_data in accounts.items():
            if existing_data.get('email') == account_data['email']:
                return False, f"Account with email {account_data['email']} already exists", None
        
        # Add account
        accounts[account_key] = account_data
        
        if self.save_accounts(accounts):
            return True, f"Account '{account_data['name']}' added successfully", account_key
        else:
            return False, "Failed to save account", None
    
    def update_account(self, account_key: str, account_data: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Update an existing account.
        
        Args:
            account_key: Key of the account to update
            account_data: New account data
            
        Returns:
            Tuple of (success, message)
        """
        accounts = self.load_accounts()
        
        if account_key not in accounts:
            return False, "Account not found"
        
        # Validate account data
        is_valid, errors = self.validator.validate_account_data(account_data)
        if not is_valid:
            return False, f"Validation errors: {', '.join(errors)}"
        
        # Check for duplicate email (excluding current account)
        for existing_key, existing_data in accounts.items():
            if (existing_key != account_key and 
                existing_data.get('email') == account_data['email']):
                return False, f"Account with email {account_data['email']} already exists"
        
        # Update account
        accounts[account_key] = account_data
        
        if self.save_accounts(accounts):
            return True, f"Account '{account_data['name']}' updated successfully"
        else:
            return False, "Failed to save account"
    
    def delete_account(self, account_key: str) -> Tuple[bool, str]:
        """
        Delete an account.
        
        Args:
            account_key: Key of the account to delete
            
        Returns:
            Tuple of (success, message)
        """
        accounts = self.load_accounts()
        
        if account_key not in accounts:
            return False, "Account not found"
        
        account_name = accounts[account_key].get('name', 'Unknown')
        
        # Remove account
        del accounts[account_key]
        
        # Remove from current profile if it was active
        current_profile = self.file_manager.get_current_profile()
        if current_profile == account_key:
            self.file_manager.remove_current_profile()
        
        if self.save_accounts(accounts):
            return True, f"Account '{account_name}' deleted successfully"
        else:
            return False, "Failed to delete account"
    
    def get_current_profile(self) -> Optional[str]:
        """
        Get current active profile.
        
        Returns:
            Current profile key if found, None otherwise
        """
        return self.file_manager.get_current_profile()
    
    def list_accounts(self) -> List[Tuple[str, Dict[str, Any]]]:
        """
        Get list of all accounts.
        
        Returns:
            List of tuples (account_key, account_data)
        """
        accounts = self.load_accounts()
        return list(accounts.items())
    
    def search_accounts(self, query: str) -> List[Tuple[str, Dict[str, Any]]]:
        """
        Search accounts by name or email.
        
        Args:
            query: Search query
            
        Returns:
            List of matching accounts
        """
        accounts = self.load_accounts()
        query = query.lower()
        
        results = []
        for key, data in accounts.items():
            name = data.get('name', '').lower()
            email = data.get('email', '').lower()
            username = data.get('username', '').lower()
            
            if (query in name or 
                query in email or 
                query in username):
                results.append((key, data))
        
        return results
    
    def validate_account_key(self, account_key: str) -> bool:
        """
        Check if account key exists.
        
        Args:
            account_key: Key to validate
            
        Returns:
            True if account exists, False otherwise
        """
        accounts = self.load_accounts()
        return account_key in accounts
