#!/usr/bin/env python3
"""
Migration script for Git Account Manager Pro v2.0.0

This script helps migrate from the old monolithic structure to the new modular architecture.
It will:
1. Backup existing configuration files
2. Move accounts.json to the new location
3. Update any necessary file paths
4. Provide instructions for the new structure

Run this script before using the new version to ensure a smooth transition.
"""

import os
import shutil
import json
import sys
from datetime import datetime


def backup_file(file_path: str, backup_dir: str = "backup") -> str:
    """
    Create a backup of a file.
    
    Args:
        file_path: Path to the file to backup
        backup_dir: Directory to store backups
        
    Returns:
        Path to the backup file
    """
    if not os.path.exists(file_path):
        return None
    
    # Create backup directory if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)
    
    # Generate backup filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.basename(file_path)
    backup_filename = f"{filename}.backup_{timestamp}"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    # Copy file to backup location
    shutil.copy2(file_path, backup_path)
    print(f"✅ Backed up {file_path} to {backup_path}")
    
    return backup_path


def migrate_accounts_file() -> bool:
    """
    Migrate accounts.json file to new structure.
    
    Returns:
        True if migration successful, False otherwise
    """
    old_accounts_file = "accounts.json"
    new_accounts_file = "accounts.json"  # Same location in v2
    
    if not os.path.exists(old_accounts_file):
        print("ℹ️ No accounts.json file found. Nothing to migrate.")
        return True
    
    try:
        # Backup the old file
        backup_path = backup_file(old_accounts_file)
        
        # Validate the JSON structure
        with open(old_accounts_file, 'r', encoding='utf-8') as f:
            accounts_data = json.load(f)
        
        print(f"✅ Found {len(accounts_data)} accounts to migrate")
        
        # The file structure is compatible, so no changes needed
        print("✅ Accounts file is compatible with v2.0.0")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Error reading accounts.json: {e}")
        return False
    except Exception as e:
        print(f"❌ Error migrating accounts file: {e}")
        return False


def migrate_theme_config() -> bool:
    """
    Migrate theme configuration to new structure.
    
    Returns:
        True if migration successful, False otherwise
    """
    old_theme_file = "theme_config.json"
    new_theme_file = "theme_config.json"  # Same location in v2
    
    if not os.path.exists(old_theme_file):
        print("ℹ️ No theme_config.json file found. Will use defaults.")
        return True
    
    try:
        # Backup the old file
        backup_path = backup_file(old_theme_file)
        
        # Validate the JSON structure
        with open(old_theme_file, 'r', encoding='utf-8') as f:
            theme_data = json.load(f)
        
        print("✅ Theme configuration is compatible with v2.0.0")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Error reading theme_config.json: {e}")
        return False
    except Exception as e:
        print(f"❌ Error migrating theme config: {e}")
        return False


def migrate_current_profile() -> bool:
    """
    Migrate current profile file to new structure.
    
    Returns:
        True if migration successful, False otherwise
    """
    old_profile_file = ".git_current_profile"
    new_profile_file = ".git_current_profile"  # Same location in v2
    
    if not os.path.exists(old_profile_file):
        print("ℹ️ No current profile file found. Nothing to migrate.")
        return True
    
    try:
        # Backup the old file
        backup_path = backup_file(old_profile_file)
        
        # Read the current profile
        with open(old_profile_file, 'r', encoding='utf-8') as f:
            current_profile = f.read().strip()
        
        print(f"✅ Current profile '{current_profile}' is compatible with v2.0.0")
        
        return True
        
    except Exception as e:
        print(f"❌ Error migrating current profile: {e}")
        return False


def cleanup_old_files() -> None:
    """
    Clean up old files that are no longer needed.
    """
    old_files = [
        "git_manager.py",  # Old monolithic file
        "t_theme.py",      # Old theme file
        "run_git_manager.bat"  # Old batch file
    ]
    
    print("\n🧹 Cleaning up old files...")
    
    for old_file in old_files:
        if os.path.exists(old_file):
            backup_path = backup_file(old_file)
            print(f"ℹ️ Old file {old_file} has been backed up to {backup_path}")
            print(f"   You can safely delete it after verifying v2.0.0 works correctly.")


def create_migration_report() -> None:
    """
    Create a migration report with instructions.
    """
    report_content = """
# Git Account Manager Pro v2.0.0 Migration Report

## Migration Completed Successfully! 🎉

Your Git Account Manager has been successfully migrated to version 2.0.0 with the new modular architecture.

## What Changed

### New Structure
- **Modular Architecture**: Code is now organized into logical modules
- **Better Separation of Concerns**: Each module has a specific responsibility
- **Improved Maintainability**: Easier to understand, modify, and extend
- **Enhanced Error Handling**: Better error messages and recovery
- **Comprehensive Documentation**: Full API and architecture documentation

### File Organization
```
src/
├── config/          # Configuration and theme management
├── core/            # Core business logic (Git & Account management)
├── ui/              # User interface components
└── utils/           # Utility functions and helpers
```

## How to Use the New Version

### Running the Application
```bash
python main.py
```

### Key Features
- All your existing accounts are preserved
- Theme preferences are maintained
- Current active profile is preserved
- Enhanced UI with better theme support
- Improved error handling and validation

## Backup Information

Your original files have been backed up to the `backup/` directory with timestamps.
You can safely delete the old files after confirming everything works correctly.

## New Features in v2.0.0

1. **Better Theme Management**: Automatic system theme detection
2. **Enhanced Validation**: Comprehensive input validation
3. **Improved Error Handling**: Better error messages and recovery
4. **Modular Architecture**: Easier to maintain and extend
5. **Comprehensive Documentation**: Full API and development guides

## Support

If you encounter any issues:
1. Check the troubleshooting section in README.md
2. Review the API documentation in docs/API.md
3. Check the architecture documentation in docs/ARCHITECTURE.md

## Next Steps

1. Test the new version with your existing accounts
2. Verify that account switching works correctly
3. Check that theme switching works as expected
4. Delete old files once you're satisfied with the new version

Enjoy the improved Git Account Manager Pro v2.0.0! 🚀
"""
    
    with open("MIGRATION_REPORT.md", "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print("📄 Migration report created: MIGRATION_REPORT.md")


def main():
    """Main migration function."""
    print("🚀 Git Account Manager Pro v2.0.0 Migration Script")
    print("=" * 60)
    print("This script will migrate your existing configuration to the new modular structure.")
    print()
    
    # Check if we're in the right directory
    if not os.path.exists("main.py"):
        print("❌ Error: main.py not found in current directory.")
        print("   Please run this script from the Git Account Manager directory.")
        return 1
    
    print("✅ Found main.py - proceeding with migration...")
    print()
    
    # Perform migrations
    success = True
    
    print("📁 Migrating configuration files...")
    success &= migrate_accounts_file()
    success &= migrate_theme_config()
    success &= migrate_current_profile()
    
    if success:
        print("\n✅ All migrations completed successfully!")
        
        # Clean up old files
        cleanup_old_files()
        
        # Create migration report
        create_migration_report()
        
        print("\n🎉 Migration completed successfully!")
        print("📄 Please read MIGRATION_REPORT.md for detailed information.")
        print("\n🚀 You can now run the new version with: python main.py")
        
        return 0
    else:
        print("\n❌ Migration failed. Please check the errors above.")
        print("   Your original files have been backed up and are safe.")
        return 1


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n⚠️ Migration interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error during migration: {e}")
        sys.exit(1)
