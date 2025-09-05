#!/usr/bin/env python3
"""
Script to create distribution packages for Git Account Manager Pro.
Creates portable package only (installer has been removed).
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def create_portable_package():
    """Create portable package."""
    print("📦 Creating Portable Package...")
    
    # Create portable directory
    portable_dir = Path("GitAccountManagerPro-Portable-v2.1.0")
    if portable_dir.exists():
        shutil.rmtree(portable_dir)
    portable_dir.mkdir()
    
    # Copy main files
    main_files = [
        "GitAccountManagerPro.exe",
        "README.md",
        "RELEASE_NOTES.md",
        "VERSION.txt",
        "LICENSE.txt"
    ]
    
    for file in main_files:
        if Path(file).exists():
            shutil.copy2(file, portable_dir / file)
            print(f"✅ {file} copied")
    
    # Note: Launcher files have been removed from this project
    
    # Note: Launcher batch file has been removed from this project
    
    # Create README for portable
    portable_readme = """# Git Account Manager Pro - Portable Version

## 🚀 Quick Start

### Method 1: Direct Execution (Recommended)
- Double-click `GitAccountManagerPro.exe` to run directly

### Method 2: Direct Execution
- Run `GitAccountManagerPro.exe` directly for immediate access

## 📁 What's Included

- `GitAccountManagerPro.exe` - Main application
- Documentation files

## 🌐 Language Support

- **🇺🇸 English** - Full English language support
- **🇮🇩 Bahasa Indonesia** - Complete Indonesian language support

## 📋 System Requirements

- **Windows 10/11** (64-bit recommended)
- **Git** (for account management features)

## 🚀 Features

- **Multi-Account Management** - Switch between multiple Git accounts
- **Automatic Configuration** - Automatically configures Git settings
- **Language Support** - English and Indonesian languages
- **Portable** - No installation required, run from any folder
- **Secure** - All data stored locally, no cloud dependencies

## 📖 Usage

1. **Extract** this portable package to any folder
2. **Run** `GitAccountManagerPro.exe`
3. **Configure** your Git accounts
4. **Switch** between accounts as needed

## 📞 Support

- **GitHub**: https://github.com/your-repo/git-account-manager-pro
- **Issues**: Report bugs and request features
- **Documentation**: Check README.md for detailed usage

## 📄 License

This software is licensed under the MIT License. See LICENSE.txt for details.

---
**Git Account Manager Pro v2.1.0** - Professional Git Account Management
"""
    
    with open(portable_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(portable_readme)
    
    print("✅ README.md created")
    
    # Create zip file
    zip_name = "GitAccountManagerPro-Portable-v2.1.0.zip"
    shutil.make_archive("GitAccountManagerPro-Portable-v2.1.0", 'zip', portable_dir)
    print(f"✅ {zip_name} created")
    
    # Cleanup
    shutil.rmtree(portable_dir)
    
    return zip_name

def create_complete_package():
    """Create complete package with both options."""
    print("📦 Creating Complete Package...")
    
    # Create complete directory
    complete_dir = Path("GitAccountManagerPro-Complete-v2.1.0")
    if complete_dir.exists():
        shutil.rmtree(complete_dir)
    complete_dir.mkdir()
    
    # Copy main files
    main_files = [
        "GitAccountManagerPro.exe",
        "README.md",
        "RELEASE_NOTES.md",
        "VERSION.txt",
        "LICENSE.txt"
    ]
    
    for file in main_files:
        if Path(file).exists():
            shutil.copy2(file, complete_dir / file)
            print(f"✅ {file} copied")
    
    # Note: Installer files have been removed from this project
    
    # Create launcher batch file
    launcher_bat = """@echo off
title Git Account Manager Pro - Launcher
echo.
echo ========================================
echo  Git Account Manager Pro - Complete
echo  Version 2.1.0 - Multi-Language Support
echo ========================================
echo.
echo Choose an option:
echo.
echo 1. Run Git Account Manager Pro
echo 2. Exit
echo.
set /p choice="Enter your choice (1-2): "

if "%choice%"=="1" (
    echo.
    echo Starting Git Account Manager Pro...
    GitAccountManagerPro.exe
) else if "%choice%"=="2" (
    echo.
    echo Goodbye!
    exit /b 0
) else (
    echo.
    echo Invalid choice. Please run the launcher again.
    pause
)
"""
    
    with open(complete_dir / "Launch.bat", 'w', encoding='utf-8') as f:
        f.write(launcher_bat)
    
    print("✅ Launch.bat created")
    
    # Create README for complete package
    complete_readme = """# Git Account Manager Pro - Complete Package

## 🚀 Quick Start

### Method 1: Launcher (Recommended)
- Double-click `Launch.bat` for easy access

### Method 2: Direct Execution
- Double-click `GitAccountManagerPro.exe` to run directly

## 📁 What's Included

- `GitAccountManagerPro.exe` - Main application
- `Launch.bat` - Easy launcher script
- Documentation files

## 🌐 Language Support

- **🇺🇸 English** - Full English language support
- **🇮🇩 Bahasa Indonesia** - Complete Indonesian language support

## 📋 System Requirements

- **Windows 10/11** (64-bit recommended)
- **Git** (for account management features)

## 🚀 Features

- **Multi-Account Management** - Switch between multiple Git accounts
- **Automatic Configuration** - Automatically configures Git settings
- **Language Support** - English and Indonesian languages
- **Portable** - No installation required, run from any folder
- **Secure** - All data stored locally, no cloud dependencies

## 📖 Usage

1. **Extract** this complete package to any folder
2. **Run** `Launch.bat` or `GitAccountManagerPro.exe`
3. **Configure** your Git accounts
4. **Switch** between accounts as needed

## 📞 Support

- **GitHub**: https://github.com/your-repo/git-account-manager-pro
- **Issues**: Report bugs and request features
- **Documentation**: Check README.md for detailed usage

## 📄 License

This software is licensed under the MIT License. See LICENSE.txt for details.

---
**Git Account Manager Pro v2.1.0** - Professional Git Account Management
"""
    
    with open(complete_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(complete_readme)
    
    print("✅ README.md created")
    
    # Create zip file
    zip_name = "GitAccountManagerPro-Complete-v2.1.0.zip"
    shutil.make_archive("GitAccountManagerPro-Complete-v2.1.0", 'zip', complete_dir)
    print(f"✅ {zip_name} created")
    
    # Cleanup
    shutil.rmtree(complete_dir)
    
    return zip_name

def main():
    """Main function."""
    print("🚀 Git Account Manager Pro - Package Creator")
    print("=" * 50)
    
    # Check if executable exists
    if not Path("GitAccountManagerPro.exe").exists():
        print("❌ GitAccountManagerPro.exe not found!")
        print("Please run this script from the project root directory.")
        return 1
    
    try:
        # Create packages
        portable_zip = create_portable_package()
        complete_zip = create_complete_package()
        
        print("\n🎉 Package creation completed successfully!")
        print(f"📦 Portable package: {portable_zip}")
        print(f"📦 Complete package: {complete_zip}")
        print("\n📁 All packages are ready for distribution!")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error creating packages: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)