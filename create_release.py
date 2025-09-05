#!/usr/bin/env python3
"""
Script to create a new release for Git Account Manager Pro.
This script helps prepare files for GitHub release.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
import json

def get_version():
    """Get current version from VERSION.txt"""
    try:
        with open("VERSION.txt", 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return "2.1.0"

def create_release_package():
    """Create release package for GitHub."""
    version = get_version()
    print(f"🚀 Creating release package for version {version}")
    
    # Create release directory
    release_dir = Path(f"GitAccountManagerPro-v{version}")
    if release_dir.exists():
        shutil.rmtree(release_dir)
    release_dir.mkdir()
    
    # Copy main executable
    if Path("GitAccountManagerPro.exe").exists():
        shutil.copy2("GitAccountManagerPro.exe", release_dir / "GitAccountManagerPro.exe")
        print("✅ Main executable copied")
    else:
        print("❌ GitAccountManagerPro.exe not found!")
        return False
    
    # Copy documentation
    docs = ["README.md", "RELEASE_NOTES.md", "LICENSE.txt", "VERSION.txt"]
    for doc in docs:
        if Path(doc).exists():
            shutil.copy2(doc, release_dir / doc)
            print(f"✅ {doc} copied")
    
    # Copy run script
    run_script = """@echo off
title Git Account Manager Pro - Launcher
echo.
echo ========================================
echo  Git Account Manager Pro v{version}
echo  Professional Git Account Management
echo ========================================
echo.
echo Starting application...
echo.

REM Check if executable exists
if not exist "GitAccountManagerPro.exe" (
    echo ERROR: GitAccountManagerPro.exe not found!
    echo Please ensure the executable is in the same folder.
    echo.
    pause
    exit /b 1
)

REM Run the application
echo Launching Git Account Manager Pro...
echo.
start "" "GitAccountManagerPro.exe"

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start the application.
    echo Please check if you have the required permissions.
    echo.
    pause
    exit /b 1
)

echo Application started successfully!
echo You can close this window now.
echo.
timeout /t 3 /nobreak >nul
exit /b 0
""".format(version=version)
    
    with open(release_dir / "run.bat", 'w', encoding='utf-8') as f:
        f.write(run_script)
    print("✅ run.bat created")
    
    # Create download README
    download_readme = f"""# 🚀 Git Account Manager Pro v{version}

**Professional Git Account Management Tool - Download & Run**

## 📥 **Cara Download & Install**

### **Metode 1: Download Langsung (Recommended)**
1. **Klik** tombol "Download" di bawah
2. **Save** file `GitAccountManagerPro.exe` ke komputer Anda
3. **Double-click** file untuk menjalankan program
4. **Selesai!** Program langsung berjalan tanpa perlu install

## 🎯 **Fitur Utama**

- ✅ **Multi-Account Management** - Kelola multiple akun Git
- ✅ **Auto Configuration** - Konfigurasi Git otomatis
- ✅ **Multi-Language** - English & Bahasa Indonesia
- ✅ **Portable** - Tidak perlu install, jalan dari folder manapun
- ✅ **Secure** - Data tersimpan lokal, aman dan private

## 📋 **System Requirements**

- **Windows 10/11** (64-bit recommended)
- **Git** (untuk fitur manajemen akun)
- **Tidak perlu Python** (sudah dikompilasi)

## 🚀 **Quick Start**

1. **Download** `GitAccountManagerPro.exe`
2. **Run** program dengan double-click
3. **Add Account** - Klik "Add Account" untuk menambah akun Git
4. **Configure** - Isi nama, email, dan username
5. **Switch** - Klik akun untuk beralih ke akun tersebut

## 🌐 **Language Support**

- **🇺🇸 English** - Full English language support
- **🇮🇩 Bahasa Indonesia** - Complete Indonesian language support

## 🔧 **Troubleshooting**

### **Program Tidak Jalan:**
- Pastikan **Windows 10/11**
- **Run as Administrator** (klik kanan → Run as administrator)
- Check **antivirus** (mungkin diblokir)

### **Git Tidak Terdeteksi:**
- Install **Git** dari [git-scm.com](https://git-scm.com/)
- Restart program setelah install Git

## 📞 **Support & Help**

- **GitHub Issues**: [Report Bug](https://github.com/densuz/Github-Account-Manager-PRO/issues)
- **Documentation**: [Full Guide](https://github.com/densuz/Github-Account-Manager-PRO/wiki)

## 📄 **License**

This software is licensed under the **MIT License**. See LICENSE.txt for details.

---

**Git Account Manager Pro v{version}** - Professional Git Account Management Made Easy! 🚀
"""
    
    with open(release_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(download_readme)
    print("✅ Download README created")
    
    # Create zip file
    zip_name = f"GitAccountManagerPro-v{version}.zip"
    shutil.make_archive(f"GitAccountManagerPro-v{version}", 'zip', release_dir)
    print(f"✅ {zip_name} created")
    
    # Cleanup
    shutil.rmtree(release_dir)
    
    return zip_name

def main():
    """Main function."""
    print("🚀 Git Account Manager Pro - Release Creator")
    print("=" * 50)
    
    # Check if executable exists
    if not Path("GitAccountManagerPro.exe").exists():
        print("❌ GitAccountManagerPro.exe not found!")
        print("Please build the executable first using build_exe.py")
        return 1
    
    try:
        # Create release package
        zip_name = create_release_package()
        
        print(f"\n🎉 Release package created successfully!")
        print(f"📦 Package: {zip_name}")
        print(f"\n📋 Next steps:")
        print(f"1. Upload {zip_name} to GitHub Releases")
        print(f"2. Or use GitHub Actions for automatic release")
        print(f"3. Share the download link with users")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error creating release package: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)