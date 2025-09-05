"""
Validation utilities for Git Account Manager Pro.
"""

import re
from typing import Dict, Any, List, Tuple


class AccountValidator:
    """Validates account data and user inputs."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate email address format.
        
        Args:
            email: Email address to validate
            
        Returns:
            True if valid, False otherwise
        """
        if not email or not isinstance(email, str):
            return False
        
        # Basic email regex pattern
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email.strip()))
    
    @staticmethod
    def validate_github_username(username: str) -> bool:
        """
        Validate GitHub username format.
        
        Args:
            username: Username to validate
            
        Returns:
            True if valid, False otherwise
        """
        if not username or not isinstance(username, str):
            return False
        
        # GitHub username rules: alphanumeric and hyphens, 1-39 characters
        pattern = r'^[a-zA-Z0-9-]{1,39}$'
        return bool(re.match(pattern, username.strip()))
    
    @staticmethod
    def validate_github_token(token: str) -> bool:
        """
        Validate GitHub personal access token format.
        
        Args:
            token: Token to validate
            
        Returns:
            True if valid, False otherwise
        """
        if not token or not isinstance(token, str):
            return False
        
        # GitHub tokens start with ghp_ and are 40 characters long
        pattern = r'^ghp_[a-zA-Z0-9]{36}$'
        return bool(re.match(pattern, token.strip()))
    
    @staticmethod
    def validate_name(name: str) -> bool:
        """
        Validate name format.
        
        Args:
            name: Name to validate
            
        Returns:
            True if valid, False otherwise
        """
        if not name or not isinstance(name, str):
            return False
        
        # Name should be at least 2 characters and contain only letters, spaces, and common punctuation
        name = name.strip()
        if len(name) < 2:
            return False
        
        # Allow letters, spaces, hyphens, apostrophes, and periods
        pattern = r'^[a-zA-Z\s\-\'\.]+$'
        return bool(re.match(pattern, name))
    
    @staticmethod
    def validate_account_data(account_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate complete account data.
        
        Args:
            account_data: Dictionary containing account information
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Check required fields
        if 'name' not in account_data or not account_data['name']:
            errors.append("Name is required")
        elif not AccountValidator.validate_name(account_data['name']):
            errors.append("Invalid name format")
        
        if 'email' not in account_data or not account_data['email']:
            errors.append("Email is required")
        elif not AccountValidator.validate_email(account_data['email']):
            errors.append("Invalid email format")
        
        # Check optional fields
        if 'username' in account_data and account_data['username']:
            if not AccountValidator.validate_github_username(account_data['username']):
                errors.append("Invalid GitHub username format")
        
        if 'token' in account_data and account_data['token']:
            if not AccountValidator.validate_github_token(account_data['token']):
                errors.append("Invalid GitHub token format")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def sanitize_account_key(name: str) -> str:
        """
        Create a sanitized key from account name.
        
        Args:
            name: Account name
            
        Returns:
            Sanitized key suitable for use as dictionary key
        """
        if not name:
            return "account"
        
        # Convert to lowercase, replace spaces with hyphens, remove special characters
        key = re.sub(r'[^a-zA-Z0-9\s-]', '', name.lower())
        key = re.sub(r'\s+', '-', key.strip())
        
        # Limit length and ensure it's not empty
        key = key[:15] if key else "account"
        
        return key
