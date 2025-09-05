#!/usr/bin/env python3
"""
Script to create distribution packages for Git Account Manager Pro.
Creates both portable and installer packages.
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
    
    # Copy launcher files
    launcher_files = [
        "portable_launcher.py",
        "installer.py"
    ]
    
    for file in launcher_files:
        if Path(file).exists():
            shutil.copy2(file, portable_dir / file)
            print(f"✅ {file} copied")
    
    # Create launcher batch file
    launcher_bat = """@echo off
title Git Account Manager Pro - Portable Launcher
echo.
echo ========================================
echo  Git Account Manager Pro - Portable
echo  Version 2.1.0 - Multi-Language Support
echo ========================================
echo.
echo Starting portable launcher...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Launching application directly...
    echo.
    GitAccountManagerPro.exe
) else (
    echo Python found. Starting launcher...
    echo.
    python portable_launcher.py
)

if errorlevel 1 (
    echo.
    echo An error occurred. Please check the console output.
    pause
)
"""
    
    with open(portable_dir / "Launch.bat", 'w', encoding='utf-8') as f:
        f.write(launcher_bat)
    
    print("✅ Launch.bat created")
    
    # Create README for portable
    portable_readme = """# Git Account Manager Pro - Portable Version

## 🚀 Quick Start

1. **Double-click `Launch.bat`** to start the portable launcher
2. **Choose your language** (English or Bahasa Indonesia)
3. **Select launch options** (portable data folder, console, etc.)
4. **Click "Launch Portable"** to run the application

## 📁 What's Included

- `GitAccountManagerPro.exe` - Main application
- `Launch.bat` - Easy launcher script
- `portable_launcher.py` - Advanced launcher with options
- `installer.py` - Full installer (if you want to install later)
- Documentation files

## 🌐 Language Support

- **🇺🇸 English** - Full English language support
- **🇮🇩 Bahasa Indonesia** - Complete Indonesian language support
- **Auto-detection** - Automatically detects your system language

## 🔧 Portable Features

- **No Installation Required** - Run from any folder
- **Portable Data** - Settings stored in local 'data' folder
- **Easy Removal** - Just delete the folder
- **Language Persistence** - Your language choice is remembered

## 🚀 Alternative Launch Methods

### Method 1: Direct Launch
- Double-click `GitAccountManagerPro.exe` to run directly

### Method 2: Launcher (Recommended)
- Double-click `Launch.bat` for options and language selection

### Method 3: Python Launcher
- Run `python portable_launcher.py` for advanced options

## 📋 System Requirements

- **Windows 10/11** (64-bit recommended)
- **Git** (for account management features)
- **Python 3.7+** (optional, for launcher features)

## 🆘 Troubleshooting

### Application Won't Start
- Ensure you have Windows 10/11
- Check if Git is installed and accessible
- Try running as administrator

### Launcher Issues
- Install Python 3.7+ for launcher features
- Or use direct launch method (double-click .exe)

### Language Not Changing
- Use the launcher to select language
- Or manually edit `data/language_config.json`

## 📞 Support

For issues, feature requests, or questions:
- GitHub: https://github.com/densuz/Github-Account-Manager-PRO
- Check README.md for detailed documentation

---

**Thank you for using Git Account Manager Pro!** 🚀
"""
    
    with open(portable_dir / "PORTABLE_README.md", 'w', encoding='utf-8') as f:
        f.write(portable_readme)
    
    print("✅ PORTABLE_README.md created")
    
    # Create ZIP
    zip_name = "GitAccountManagerPro-Portable-v2.1.0.zip"
    if Path(zip_name).exists():
        Path(zip_name).unlink()
    
    shutil.make_archive("GitAccountManagerPro-Portable-v2.1.0", 'zip', portable_dir)
    print(f"✅ {zip_name} created")
    
    # Cleanup
    shutil.rmtree(portable_dir)
    
    return zip_name

def create_installer_package():
    """Create installer package."""
    print("📦 Creating Installer Package...")
    
    # Create installer directory
    installer_dir = Path("GitAccountManagerPro-Installer-v2.1.0")
    if installer_dir.exists():
        shutil.rmtree(installer_dir)
    installer_dir.mkdir()
    
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
            shutil.copy2(file, installer_dir / file)
            print(f"✅ {file} copied")
    
    # Copy installer files
    installer_files = [
        "installer.py",
        "installer.nsi",
        "portable_launcher.py"
    ]
    
    for file in installer_files:
        if Path(file).exists():
            shutil.copy2(file, installer_dir / file)
            print(f"✅ {file} copied")
    
    # Create installer batch file
    installer_bat = """@echo off
title Git Account Manager Pro - Installer
echo.
echo ========================================
echo  Git Account Manager Pro - Installer
echo  Version 2.1.0 - Multi-Language Support
echo ========================================
echo.
echo Starting installer...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Please install Python 3.7+ to run the installer.
    echo.
    echo You can also use the NSIS installer if available:
    echo - Look for GitAccountManagerPro-Setup.exe
    echo.
    pause
    exit /b 1
) else (
    echo Python found. Starting installer...
    echo.
    python installer.py
)

if errorlevel 1 (
    echo.
    echo Installer encountered an error.
    pause
)
"""
    
    with open(installer_dir / "Install.bat", 'w', encoding='utf-8') as f:
        f.write(installer_bat)
    
    print("✅ Install.bat created")
    
    # Create README for installer
    installer_readme = """# Git Account Manager Pro - Installer Package

## 🚀 Installation Options

### Option 1: Python Installer (Recommended)
1. **Double-click `Install.bat`** to start the installer
2. **Choose installation type**:
   - **Portable Installation** - No system changes, run from any folder
   - **Full Installation** - Install to Program Files with shortcuts
3. **Select installation location**
4. **Choose options** (desktop shortcut, start menu, etc.)
5. **Click Install** to begin installation

### Option 2: NSIS Installer (Advanced)
1. **Compile the NSIS installer** using `installer.nsi`
2. **Run the generated setup.exe**
3. **Follow the installation wizard**

## 📁 What's Included

- `GitAccountManagerPro.exe` - Main application
- `Install.bat` - Easy installer launcher
- `installer.py` - Python-based installer with GUI
- `installer.nsi` - NSIS installer script
- `portable_launcher.py` - Portable launcher (for portable mode)
- Documentation files

## 🌐 Language Support

- **🇺🇸 English** - Full English language support
- **🇮🇩 Bahasa Indonesia** - Complete Indonesian language support
- **Auto-detection** - Automatically detects your system language

## 🔧 Installation Types

### Portable Installation
- **No system changes** - No registry modifications
- **Run from any folder** - Copy to USB, cloud storage, etc.
- **Easy removal** - Just delete the folder
- **Portable data** - Settings stored locally

### Full Installation
- **System integration** - Install to Program Files
- **Desktop shortcut** - Easy access from desktop
- **Start Menu entry** - Access from Start Menu
- **Proper uninstaller** - Clean removal via Control Panel
- **Windows integration** - Better system integration

## 📋 System Requirements

- **Windows 10/11** (64-bit recommended)
- **Git** (for account management features)
- **Python 3.7+** (for Python installer)
- **NSIS** (optional, for compiling NSIS installer)

## 🛠️ Building NSIS Installer

If you want to create a professional Windows installer:

1. **Install NSIS** from https://nsis.sourceforge.io/
2. **Right-click on `installer.nsi`**
3. **Select "Compile NSIS Script"**
4. **Run the generated `GitAccountManagerPro-Setup.exe`**

## 🆘 Troubleshooting

### Python Installer Issues
- Ensure Python 3.7+ is installed
- Check if Python is in your system PATH
- Try running as administrator

### NSIS Installer Issues
- Install NSIS from the official website
- Ensure all required files are present
- Check NSIS documentation for advanced options

### Application Won't Start
- Ensure you have Windows 10/11
- Check if Git is installed and accessible
- Try running as administrator

## 📞 Support

For issues, feature requests, or questions:
- GitHub: https://github.com/densuz/Github-Account-Manager-PRO
- Check README.md for detailed documentation

---

**Thank you for using Git Account Manager Pro!** 🚀
"""
    
    with open(installer_dir / "INSTALLER_README.md", 'w', encoding='utf-8') as f:
        f.write(installer_readme)
    
    print("✅ INSTALLER_README.md created")
    
    # Create ZIP
    zip_name = "GitAccountManagerPro-Installer-v2.1.0.zip"
    if Path(zip_name).exists():
        Path(zip_name).unlink()
    
    shutil.make_archive("GitAccountManagerPro-Installer-v2.1.0", 'zip', installer_dir)
    print(f"✅ {zip_name} created")
    
    # Cleanup
    shutil.rmtree(installer_dir)
    
    return zip_name

def create_complete_package():
    """Create complete package with both options."""
    print("📦 Creating Complete Package...")
    
    # Create complete directory
    complete_dir = Path("GitAccountManagerPro-Complete-v2.1.0")
    if complete_dir.exists():
        shutil.rmtree(complete_dir)
    complete_dir.mkdir()
    
    # Copy all files
    all_files = [
        "GitAccountManagerPro.exe",
        "README.md",
        "RELEASE_NOTES.md",
        "VERSION.txt",
        "LICENSE.txt",
        "installer.py",
        "installer.nsi",
        "portable_launcher.py"
    ]
    
    for file in all_files:
        if Path(file).exists():
            shutil.copy2(file, complete_dir / file)
            print(f"✅ {file} copied")
    
    # Create launcher batch
    launcher_bat = """@echo off
title Git Account Manager Pro - Complete Package
echo.
echo ========================================
echo  Git Account Manager Pro - Complete
echo  Version 2.1.0 - Multi-Language Support
echo ========================================
echo.
echo Choose your preferred installation method:
echo.
echo 1. Launch Portable Version (No installation)
echo 2. Run Full Installer (System installation)
echo 3. Exit
echo.
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo.
    echo Starting portable launcher...
    python portable_launcher.py
) else if "%choice%"=="2" (
    echo.
    echo Starting installer...
    python installer.py
) else if "%choice%"=="3" (
    echo.
    echo Goodbye!
    exit /b 0
) else (
    echo.
    echo Invalid choice. Please run again.
    pause
)
"""
    
    with open(complete_dir / "Launch.bat", 'w', encoding='utf-8') as f:
        f.write(launcher_bat)
    
    print("✅ Launch.bat created")
    
    # Create complete README
    complete_readme = """# Git Account Manager Pro - Complete Package

## 🎉 Welcome to Git Account Manager Pro v2.1.0!

This complete package includes everything you need to run Git Account Manager Pro in any way you prefer.

## 🚀 Quick Start

**Double-click `Launch.bat`** and choose your preferred method:

1. **Portable Version** - Run without installation
2. **Full Installer** - Install to your system
3. **Exit** - Close the launcher

## 📦 What's Included

### Core Application
- `GitAccountManagerPro.exe` - Main application executable
- `README.md` - Complete documentation
- `RELEASE_NOTES.md` - Detailed release notes
- `VERSION.txt` - Version information
- `LICENSE.txt` - License agreement

### Installation Options
- `Launch.bat` - Easy launcher with options
- `installer.py` - Python-based installer with GUI
- `installer.nsi` - NSIS installer script (for advanced users)
- `portable_launcher.py` - Portable launcher with language detection

## 🌐 Language Support

- **🇺🇸 English** - Full English language support
- **🇮🇩 Bahasa Indonesia** - Complete Indonesian language support
- **Auto-detection** - Automatically detects your system language
- **Easy switching** - Change language anytime

## 🔧 Installation Methods

### Method 1: Portable (Recommended for beginners)
- **No installation required**
- **Run from any folder**
- **No system changes**
- **Easy to remove**
- **Perfect for USB drives**

### Method 2: Full Installation
- **System integration**
- **Desktop shortcuts**
- **Start Menu entry**
- **Proper uninstaller**
- **Windows integration**

### Method 3: Advanced (NSIS)
- **Professional installer**
- **Windows-standard installation**
- **Automatic uninstaller**
- **System integration**

## 📋 System Requirements

- **Windows 10/11** (64-bit recommended)
- **Git** (for account management features)
- **Python 3.7+** (for installer and launcher features)

## 🚀 Getting Started

### For First-Time Users
1. **Double-click `Launch.bat`**
2. **Choose "1" for Portable Version**
3. **Select your language**
4. **Click "Launch Portable"**
5. **Start managing your Git accounts!**

### For System Installation
1. **Double-click `Launch.bat`**
2. **Choose "2" for Full Installer**
3. **Follow the installation wizard**
4. **Choose installation type and options**
5. **Launch from desktop or Start Menu**

### For Advanced Users
1. **Install NSIS** from https://nsis.sourceforge.io/
2. **Compile `installer.nsi`** to create professional installer
3. **Run the generated setup.exe**

## 🆘 Troubleshooting

### Python Not Found
- Install Python 3.7+ from https://python.org
- Ensure Python is added to system PATH
- Or use direct launch: double-click `GitAccountManagerPro.exe`

### Application Won't Start
- Ensure you have Windows 10/11
- Check if Git is installed: `git --version`
- Try running as administrator

### Language Issues
- Use the launcher to select language
- Or manually edit language settings in data folder

## 📞 Support & Updates

- **GitHub Repository**: https://github.com/densuz/Github-Account-Manager-PRO
- **Version**: 2.1.0
- **Release Date**: September 6, 2025
- **License**: Open Source

## 🎯 Features

- ✅ **Multi-Git Account Management**
- ✅ **Easy Account Switching**
- ✅ **Secure Token Storage**
- ✅ **Multi-Language Support** (English & Bahasa Indonesia)
- ✅ **Theme Support** (Dark, Light, System)
- ✅ **Portable & Installer Options**
- ✅ **Modern, Clean Interface**

---

**Thank you for using Git Account Manager Pro!** 🚀

If you find this tool helpful, please consider starring the repository on GitHub!
"""
    
    with open(complete_dir / "COMPLETE_README.md", 'w', encoding='utf-8') as f:
        f.write(complete_readme)
    
    print("✅ COMPLETE_README.md created")
    
    # Create ZIP
    zip_name = "GitAccountManagerPro-Complete-v2.1.0.zip"
    if Path(zip_name).exists():
        Path(zip_name).unlink()
    
    shutil.make_archive("GitAccountManagerPro-Complete-v2.1.0", 'zip', complete_dir)
    print(f"✅ {zip_name} created")
    
    # Cleanup
    shutil.rmtree(complete_dir)
    
    return zip_name

def main():
    """Main package creation process."""
    print("🚀 Git Account Manager Pro - Package Creator")
    print("=" * 50)
    
    # Check if executable exists
    if not Path("GitAccountManagerPro.exe").exists():
        print("❌ GitAccountManagerPro.exe not found!")
        print("Please run this script from the same folder as the executable.")
        return 1
    
    packages_created = []
    
    # Create portable package
    try:
        portable_zip = create_portable_package()
        packages_created.append(portable_zip)
    except Exception as e:
        print(f"❌ Failed to create portable package: {e}")
    
    # Create installer package
    try:
        installer_zip = create_installer_package()
        packages_created.append(installer_zip)
    except Exception as e:
        print(f"❌ Failed to create installer package: {e}")
    
    # Create complete package
    try:
        complete_zip = create_complete_package()
        packages_created.append(complete_zip)
    except Exception as e:
        print(f"❌ Failed to create complete package: {e}")
    
    print("\n🎉 Package creation completed!")
    print("📦 Created packages:")
    for package in packages_created:
        size = Path(package).stat().st_size / (1024 * 1024)  # MB
        print(f"  📄 {package} ({size:.1f} MB)")
    
    print("\n📋 Package descriptions:")
    print("  🚀 Portable - Run without installation")
    print("  🔧 Installer - System installation with options")
    print("  📦 Complete - All options in one package")
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
