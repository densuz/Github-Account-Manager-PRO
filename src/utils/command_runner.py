"""
Command execution utilities for Git Account Manager Pro.
"""

import subprocess
from typing import Optional


class CommandRunner:
    """Handles command execution with proper error handling."""
    
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
    
    def run_command(self, cmd: str) -> str:
        """
        Run a shell command with improved error handling.
        
        Args:
            cmd: Command to execute
            
        Returns:
            Command output as string
            
        Raises:
            Exception: If command fails or times out
        """
        try:
            result = subprocess.run(
                cmd, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=self.timeout
            )
            
            if result.returncode != 0:
                error_msg = result.stderr.strip() if result.stderr.strip() else "Unknown error"
                raise Exception(f"Command '{cmd}' failed with code {result.returncode}: {error_msg}")
            
            return result.stdout.strip()
            
        except subprocess.TimeoutExpired:
            raise Exception(f"Command '{cmd}' timed out after {self.timeout} seconds")
        except Exception as e:
            if "Command" in str(e):
                raise e
            else:
                raise Exception(f"Failed to execute command '{cmd}': {str(e)}")
    
    def run_git_command(self, git_cmd: str) -> str:
        """
        Run a git command with proper error handling.
        
        Args:
            git_cmd: Git command to execute (without 'git' prefix)
            
        Returns:
            Command output as string
            
        Raises:
            Exception: If command fails
        """
        full_cmd = f"git {git_cmd}"
        return self.run_command(full_cmd)
    
    def check_git_installed(self) -> bool:
        """
        Check if Git is installed and accessible.
        
        Returns:
            True if Git is available, False otherwise
        """
        try:
            self.run_command("git --version")
            return True
        except:
            return False
