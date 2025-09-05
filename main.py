#!/usr/bin/env python3
"""
Git Account Manager Pro - Main Application Entry Point

A professional Git account management tool with modular architecture.
Allows users to manage multiple GitHub accounts and switch between them easily.

Author: Git Account Manager Team
Version: 2.0.0
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.ui.main_window import MainWindow
from src.core.git_manager import GitManager
from src.utils.command_runner import CommandRunner


def check_dependencies():
    """Check if all required dependencies are available."""
    try:
        # Check if tkinter is available
        import tkinter
        print("✅ Tkinter is available")
        
        # Check if Git is installed
        command_runner = CommandRunner()
        if command_runner.check_git_installed():
            print("✅ Git is installed and available")
        else:
            print("❌ Git is not installed or not in PATH")
            messagebox.showerror(
                "Git Not Found", 
                "Git is not installed or not accessible from command line.\n"
                "Please install Git and ensure it's in your system PATH."
            )
            return False
        
        return True
        
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        messagebox.showerror(
            "Missing Dependency", 
            f"Required dependency is missing:\n{e}\n"
            "Please install the required dependencies."
        )
        return False
    except Exception as e:
        print(f"❌ Error checking dependencies: {e}")
        messagebox.showerror(
            "Dependency Check Failed", 
            f"Failed to check dependencies:\n{e}"
        )
        return False


def main():
    """Main application entry point."""
    print("🚀 Starting Git Account Manager Pro v2.0.0")
    print("=" * 50)
    
    try:
        # Check dependencies
        if not check_dependencies():
            print("❌ Dependency check failed. Exiting.")
            return 1
        
        print("✅ All dependencies are available")
        print("🎨 Initializing application...")
        
        # Create and run the main window
        app = MainWindow()
        print("✅ Application initialized successfully")
        print("🖥️ Starting GUI...")
        
        app.run()
        
        print("👋 Application closed successfully")
        return 0
        
    except KeyboardInterrupt:
        print("\n⚠️ Application interrupted by user (Ctrl+C)")
        return 0
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        try:
            messagebox.showerror(
                "Fatal Error", 
                f"Application encountered a fatal error:\n{e}\n\n"
                "Please check the console output for more details."
            )
        except:
            pass  # If messagebox fails, just print the error
        return 1
    finally:
        print("=" * 50)
        print("Git Account Manager Pro session ended.")


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
