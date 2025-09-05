#!/usr/bin/env python3
"""
Script to create GitHub release for Git Account Manager Pro.
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def get_git_remote_url():
    """Get the GitHub repository URL."""
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_current_version():
    """Get current version from git tags."""
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "v2.1.0"  # Default version

def create_git_tag(version):
    """Create a git tag for the release."""
    try:
        # Check if tag already exists
        result = subprocess.run(
            ["git", "tag", "-l", version],
            capture_output=True,
            text=True
        )
        
        if result.stdout.strip():
            print(f"⚠️ Tag {version} already exists")
            return True
        
        # Create and push tag
        subprocess.run(["git", "tag", "-a", version, "-m", f"Release {version}"], check=True)
        subprocess.run(["git", "push", "origin", version], check=True)
        print(f"✅ Tag {version} created and pushed")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create tag: {e}")
        return False

def create_github_release():
    """Create GitHub release using GitHub CLI or manual instructions."""
    print("📋 GitHub Release Instructions:")
    print("=" * 50)
    
    # Get repository info
    remote_url = get_git_remote_url()
    if remote_url:
        if "github.com" in remote_url:
            repo_name = remote_url.split("/")[-1].replace(".git", "")
            print(f"📁 Repository: {repo_name}")
        else:
            print("⚠️ Not a GitHub repository")
    else:
        print("⚠️ No remote repository found")
    
    version = "v2.1.0"
    
    print(f"\n🏷️ Version: {version}")
    print(f"📅 Release Date: September 6, 2025")
    
    print("\n📝 Release Title:")
    print("Git Account Manager Pro v2.1.0 - Multi-Language Support")
    
    print("\n📄 Release Description:")
    print("""
## 🌐 New Features

### Multi-Language Support
- **English** 🇺🇸 - Full English language support
- **Bahasa Indonesia** 🇮🇩 - Complete Indonesian language support
- **Language Switcher** - Easy language switching with flag icons
- **Persistent Language Settings** - Language preference is saved and remembered

### Enhanced User Interface
- Language switcher buttons with country flags
- Consistent styling with existing theme system
- Real-time language switching (requires app restart)
- Improved user experience with visual language indicators

## 🔧 Technical Improvements

### New Components Added
- `LanguageManager` - Centralized language management system
- `Translation System` - Comprehensive translation framework
- `Language Configuration` - Persistent language settings storage
- `UI Language Components` - Reusable language switcher components

## 📦 Downloads

### Windows Executable
- **GitAccountManagerPro.exe** - Standalone executable (no installation required)
- **run.bat** - Easy execution script
- **VERSION.txt** - Version and feature information

### Source Code
- Complete source code with all language features
- Python 3.7+ compatible
- All dependencies listed in requirements.txt

## 🚀 Installation

### For Executable Users:
1. Download the release files
2. Extract to desired location
3. Run `GitAccountManagerPro.exe` or `run.bat`
4. No additional setup required

### For Developers:
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

## 🔄 System Requirements
- Windows 10/11 (for executable)
- Python 3.7+ (for source code)
- Git (for account management features)

## 📋 What's New
- Complete Indonesian language support
- Language switcher with flag icons
- Persistent language preferences
- Enhanced user interface
- Improved error handling
- Better user feedback

## 🐛 Bug Fixes
- Improved error message handling
- Better user feedback for language switching
- Enhanced configuration file management
- More robust translation fallback system

## 📞 Support
For issues, feature requests, or questions, please visit the GitHub repository.
""")
    
    print("\n📁 Files to Upload:")
    print("- GitAccountManagerPro.exe (Windows executable)")
    print("- run.bat (Execution script)")
    print("- VERSION.txt (Version information)")
    print("- Source code (zip)")
    
    print("\n🔗 Manual Release Creation:")
    print("1. Go to your GitHub repository")
    print("2. Click 'Releases' → 'Create a new release'")
    print("3. Create tag: v2.1.0")
    print("4. Use the title and description above")
    print("5. Upload the files from the 'release' folder")
    print("6. Mark as 'Latest release'")
    print("7. Publish the release")
    
    return True

def main():
    """Main release creation process."""
    print("🚀 Git Account Manager Pro - Release Creator")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not Path(".git").exists():
        print("❌ Not in a git repository")
        return 1
    
    # Create git tag
    version = "v2.1.0"
    if not create_git_tag(version):
        print("⚠️ Continuing without git tag...")
    
    # Create GitHub release instructions
    create_github_release()
    
    print("\n✅ Release preparation completed!")
    print("📋 Follow the instructions above to create the GitHub release")
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
