#!/usr/bin/env python3
"""
Build script for creating Git Account Manager Pro executable.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_pyinstaller():
    """Check if PyInstaller is installed."""
    try:
        import PyInstaller
        print("✅ PyInstaller is available")
        return True
    except ImportError:
        print("❌ PyInstaller not found. Installing...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install PyInstaller")
            return False

def create_spec_file():
    """Create PyInstaller spec file for better control."""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src', 'src'),
        ('data', 'data'),
        ('README.md', '.'),
        ('RELEASE_NOTES.md', '.'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'json',
        'os',
        'sys',
        'pyperclip',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='GitAccountManagerPro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
'''
    
    with open('GitAccountManagerPro.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✅ PyInstaller spec file created")

def build_executable():
    """Build the executable using PyInstaller."""
    print("🔨 Building executable...")
    
    try:
        # Use the spec file for building
        cmd = [sys.executable, "-m", "PyInstaller", "--clean", "GitAccountManagerPro.spec"]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Executable built successfully!")
            return True
        else:
            print(f"❌ Build failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error building executable: {e}")
        return False

def create_distribution():
    """Create distribution folder with executable and required files."""
    print("📦 Creating distribution package...")
    
    dist_dir = Path("dist")
    release_dir = Path("release")
    
    # Create release directory
    if release_dir.exists():
        shutil.rmtree(release_dir)
    release_dir.mkdir()
    
    # Copy executable
    exe_path = dist_dir / "GitAccountManagerPro.exe"
    if exe_path.exists():
        shutil.copy2(exe_path, release_dir / "GitAccountManagerPro.exe")
        print("✅ Executable copied to release folder")
    else:
        print("❌ Executable not found in dist folder")
        return False
    
    # Copy additional files
    files_to_copy = [
        "README.md",
        "RELEASE_NOTES.md",
        "requirements.txt"
    ]
    
    for file in files_to_copy:
        if Path(file).exists():
            shutil.copy2(file, release_dir / file)
            print(f"✅ {file} copied to release folder")
    
    # Create version info file
    version_info = """Git Account Manager Pro v2.1.0
Build Date: January 6, 2025

Features:
- Multi-language support (English & Bahasa Indonesia)
- Theme switching (Dark, Light, System)
- Git account management
- Easy account switching

System Requirements:
- Windows 10/11
- Git (for account management features)

Installation:
1. Download and extract this package
2. Run GitAccountManagerPro.exe
3. No additional installation required

For support and updates, visit the GitHub repository.
"""
    
    with open(release_dir / "VERSION.txt", 'w', encoding='utf-8') as f:
        f.write(version_info)
    
    print("✅ Version info file created")
    
    # Create batch file for easy execution
    batch_content = """@echo off
echo Starting Git Account Manager Pro...
echo.
GitAccountManagerPro.exe
if errorlevel 1 (
    echo.
    echo Application encountered an error.
    echo Please check the console output for details.
    pause
)
"""
    
    with open(release_dir / "run.bat", 'w', encoding='utf-8') as f:
        f.write(batch_content)
    
    print("✅ Batch file created")
    
    return True

def main():
    """Main build process."""
    print("🚀 Git Account Manager Pro - Build Script")
    print("=" * 50)
    
    # Check PyInstaller
    if not check_pyinstaller():
        return 1
    
    # Create spec file
    create_spec_file()
    
    # Build executable
    if not build_executable():
        return 1
    
    # Create distribution
    if not create_distribution():
        return 1
    
    print("\n🎉 Build completed successfully!")
    print("📁 Release files are in the 'release' folder")
    print("📄 Executable: release/GitAccountManagerPro.exe")
    print("📄 Run script: release/run.bat")
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
