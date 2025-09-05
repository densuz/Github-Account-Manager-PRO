#!/usr/bin/env python3
"""
Git Account Manager Pro - Installer Script
Allows users to choose between Portable or Full Installation
"""

import os
import sys
import shutil
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import subprocess
import json

class InstallerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Git Account Manager Pro - Installer")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Installation type
        self.install_type = tk.StringVar(value="portable")
        self.install_path = tk.StringVar()
        self.create_desktop_shortcut = tk.BooleanVar(value=True)
        self.create_start_menu = tk.BooleanVar(value=True)
        
        self.create_ui()
    
    def center_window(self):
        """Center the installer window."""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"600x500+{x}+{y}")
    
    def create_ui(self):
        """Create the installer UI."""
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_frame)
        
        # Installation type selection
        self.create_install_type_section(main_frame)
        
        # Installation path
        self.create_path_section(main_frame)
        
        # Options
        self.create_options_section(main_frame)
        
        # Buttons
        self.create_buttons(main_frame)
    
    def create_header(self, parent):
        """Create installer header."""
        header_frame = tk.Frame(parent, bg="#f0f0f0")
        header_frame.pack(fill="x", pady=(0, 20))
        
        # Icon and title
        title_frame = tk.Frame(header_frame, bg="#f0f0f0")
        title_frame.pack()
        
        icon_label = tk.Label(
            title_frame,
            text="🚀",
            font=("Segoe UI Emoji", 32),
            bg="#f0f0f0"
        )
        icon_label.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="Git Account Manager Pro",
            font=("Segoe UI", 20, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        title_label.pack(side="left")
        
        subtitle_label = tk.Label(
            header_frame,
            text="Installer v2.1.0 - Multi-Language Support",
            font=("Segoe UI", 12),
            bg="#f0f0f0",
            fg="#7f8c8d"
        )
        subtitle_label.pack(pady=(10, 0))
    
    def create_install_type_section(self, parent):
        """Create installation type selection."""
        type_frame = tk.LabelFrame(
            parent,
            text="⚙️ Installation Type",
            font=("Segoe UI", 13, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            relief="solid",
            bd=2
        )
        type_frame.pack(fill="x", pady=(0, 20))
        
        # Type container
        type_container = tk.Frame(type_frame, bg="#f8f9fa")
        type_container.pack(fill="x", padx=25, pady=20)
        
        # Title label
        title_label = tk.Label(
            type_container,
            text="Choose Installation Method",
            font=("Segoe UI", 12, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50"
        )
        title_label.pack(anchor="w", pady=(0, 15))
        
        # Portable option
        portable_frame = tk.Frame(type_container, bg="#f8f9fa")
        portable_frame.pack(fill="x", pady=(0, 15))
        
        portable_radio = tk.Radiobutton(
            portable_frame,
            text="📦 Portable Installation",
            variable=self.install_type,
            value="portable",
            font=("Segoe UI", 12, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            selectcolor="#f8f9fa",
            activebackground="#f8f9fa",
            activeforeground="#2c3e50",
            command=self.on_install_type_change
        )
        portable_radio.pack(anchor="w")
        
        portable_desc = tk.Label(
            portable_frame,
            text="  • No system installation required\n  • Run from any folder\n  • No registry changes\n  • Easy to uninstall",
            font=("Segoe UI", 10),
            bg="#f8f9fa",
            fg="#7f8c8d",
            justify="left"
        )
        portable_desc.pack(anchor="w", padx=(25, 0), pady=(5, 0))
        
        # Full installation option
        full_frame = tk.Frame(type_container, bg="#f8f9fa")
        full_frame.pack(fill="x", pady=(0, 5))
        
        full_radio = tk.Radiobutton(
            full_frame,
            text="🏠 Full Installation",
            variable=self.install_type,
            value="full",
            font=("Segoe UI", 12, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            selectcolor="#f8f9fa",
            activebackground="#f8f9fa",
            activeforeground="#2c3e50",
            command=self.on_install_type_change
        )
        full_radio.pack(anchor="w")
        
        full_desc = tk.Label(
            full_frame,
            text="  • Install to Program Files\n  • Desktop and Start Menu shortcuts\n  • Windows integration\n  • Proper uninstaller",
            font=("Segoe UI", 10),
            bg="#f8f9fa",
            fg="#7f8c8d",
            justify="left"
        )
        full_desc.pack(anchor="w", padx=(25, 0), pady=(5, 0))
    
    def create_path_section(self, parent):
        """Create installation path section."""
        path_frame = tk.LabelFrame(
            parent,
            text="📁 Installation Location",
            font=("Segoe UI", 13, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            relief="solid",
            bd=2
        )
        path_frame.pack(fill="x", pady=(0, 20))
        
        # Path input container
        path_container = tk.Frame(path_frame, bg="#f8f9fa")
        path_container.pack(fill="x", padx=25, pady=20)
        
        # Title label
        title_label = tk.Label(
            path_container,
            text="Choose Installation Directory",
            font=("Segoe UI", 12, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50"
        )
        title_label.pack(anchor="w", pady=(0, 10))
        
        # Path input frame
        path_input_frame = tk.Frame(path_container, bg="#f8f9fa")
        path_input_frame.pack(fill="x", pady=(0, 10))
        
        # Path label
        path_label = tk.Label(
            path_input_frame,
            text="Install to:",
            font=("Segoe UI", 11, "bold"),
            bg="#f8f9fa",
            fg="#34495e"
        )
        path_label.pack(anchor="w", pady=(0, 8))
        
        # Entry and button frame
        entry_button_frame = tk.Frame(path_input_frame, bg="#f8f9fa")
        entry_button_frame.pack(fill="x")
        
        # Path entry
        self.path_entry = tk.Entry(
            entry_button_frame,
            textvariable=self.install_path,
            font=("Segoe UI", 11),
            state="readonly",
            relief="solid",
            bd=2,
            bg="white",
            fg="#2c3e50",
            insertbackground="#2c3e50"
        )
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 12))
        
        # Browse button
        browse_btn = tk.Button(
            entry_button_frame,
            text="📂 Browse...",
            command=self.browse_path,
            font=("Segoe UI", 10, "bold"),
            bg="#3498db",
            fg="white",
            relief="flat",
            padx=25,
            pady=8,
            cursor="hand2",
            bd=0
        )
        browse_btn.pack(side="right")
        
        # Path description
        path_desc = tk.Label(
            path_container,
            text="💡 Choose where to install Git Account Manager Pro on your computer.\n   The application will be installed in the selected directory.",
            font=("Segoe UI", 10),
            bg="#f8f9fa",
            fg="#7f8c8d",
            wraplength=500,
            justify="left"
        )
        path_desc.pack(anchor="w", pady=(10, 0))
        
        # Set default path
        self.set_default_path()
    
    def create_options_section(self, parent):
        """Create installation options."""
        options_frame = tk.LabelFrame(
            parent,
            text="🔧 Installation Options",
            font=("Segoe UI", 13, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            relief="solid",
            bd=2
        )
        options_frame.pack(fill="x", pady=(0, 20))
        
        # Options container
        options_container = tk.Frame(options_frame, bg="#f8f9fa")
        options_container.pack(fill="x", padx=25, pady=20)
        
        # Title label
        title_label = tk.Label(
            options_container,
            text="Additional Installation Options",
            font=("Segoe UI", 12, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50"
        )
        title_label.pack(anchor="w", pady=(0, 15))
        
        # Desktop shortcut
        desktop_frame = tk.Frame(options_container, bg="#f8f9fa")
        desktop_frame.pack(fill="x", pady=(0, 12))
        
        desktop_check = tk.Checkbutton(
            desktop_frame,
            text="🖥️ Create Desktop Shortcut",
            variable=self.create_desktop_shortcut,
            font=("Segoe UI", 11, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            selectcolor="#f8f9fa",
            activebackground="#f8f9fa",
            activeforeground="#2c3e50"
        )
        desktop_check.pack(anchor="w")
        
        desktop_desc = tk.Label(
            desktop_frame,
            text="  • Creates a shortcut on your desktop for easy access",
            font=("Segoe UI", 10),
            bg="#f8f9fa",
            fg="#7f8c8d"
        )
        desktop_desc.pack(anchor="w", padx=(25, 0))
        
        # Start Menu shortcut
        startmenu_frame = tk.Frame(options_container, bg="#f8f9fa")
        startmenu_frame.pack(fill="x", pady=(0, 12))
        
        startmenu_check = tk.Checkbutton(
            startmenu_frame,
            text="📋 Create Start Menu Entry",
            variable=self.create_start_menu,
            font=("Segoe UI", 11, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            selectcolor="#f8f9fa",
            activebackground="#f8f9fa",
            activeforeground="#2c3e50"
        )
        startmenu_check.pack(anchor="w")
        
        startmenu_desc = tk.Label(
            startmenu_frame,
            text="  • Adds the application to your Start Menu Programs folder",
            font=("Segoe UI", 10),
            bg="#f8f9fa",
            fg="#7f8c8d"
        )
        startmenu_desc.pack(anchor="w", padx=(25, 0))
    
    def create_buttons(self, parent):
        """Create action buttons."""
        button_frame = tk.Frame(parent, bg="#f0f0f0")
        button_frame.pack(fill="x", pady=(20, 0))
        
        # Cancel button
        cancel_btn = tk.Button(
            button_frame,
            text="Cancel",
            command=self.cancel_install,
            font=("Segoe UI", 10),
            bg="#95a5a6",
            fg="white",
            relief="flat",
            padx=20,
            pady=8
        )
        cancel_btn.pack(side="right", padx=(10, 0))
        
        # Install button
        install_btn = tk.Button(
            button_frame,
            text="Install",
            command=self.start_install,
            font=("Segoe UI", 10, "bold"),
            bg="#27ae60",
            fg="white",
            relief="flat",
            padx=20,
            pady=8
        )
        install_btn.pack(side="right")
    
    def on_install_type_change(self):
        """Handle installation type change."""
        self.set_default_path()
    
    def set_default_path(self):
        """Set default installation path based on type."""
        if self.install_type.get() == "portable":
            # Default to Desktop for portable
            desktop = Path.home() / "Desktop"
            self.install_path.set(str(desktop / "GitAccountManagerPro"))
        else:
            # Default to Program Files for full installation
            program_files = Path("C:/Program Files")
            self.install_path.set(str(program_files / "GitAccountManagerPro"))
    
    def browse_path(self):
        """Browse for installation path."""
        from tkinter import filedialog
        
        if self.install_type.get() == "portable":
            # For portable, select a folder
            path = filedialog.askdirectory(
                title="Select Installation Folder",
                initialdir=str(Path.home() / "Desktop")
            )
        else:
            # For full installation, select Program Files
            path = filedialog.askdirectory(
                title="Select Installation Folder",
                initialdir="C:/Program Files"
            )
        
        if path:
            self.install_path.set(path)
    
    def cancel_install(self):
        """Cancel installation."""
        if messagebox.askyesno("Cancel Installation", "Are you sure you want to cancel the installation?"):
            self.root.destroy()
    
    def start_install(self):
        """Start the installation process."""
        install_path = Path(self.install_path.get())
        
        if not install_path.parent.exists():
            messagebox.showerror("Error", "The parent directory does not exist!")
            return
        
        # Show installation progress
        self.show_progress()
        
        try:
            if self.install_type.get() == "portable":
                self.install_portable(install_path)
            else:
                self.install_full(install_path)
            
            self.show_success()
            
        except Exception as e:
            messagebox.showerror("Installation Error", f"Installation failed:\n{str(e)}")
    
    def show_progress(self):
        """Show installation progress."""
        # Hide main UI
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Progress UI
        progress_frame = tk.Frame(self.root, bg="#f0f0f0")
        progress_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(
            progress_frame,
            text="Installing Git Account Manager Pro...",
            font=("Segoe UI", 16, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        ).pack(pady=(0, 20))
        
        self.progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(
            progress_frame,
            variable=self.progress_var,
            maximum=100
        )
        progress_bar.pack(fill="x", pady=(0, 10))
        
        self.status_label = tk.Label(
            progress_frame,
            text="Preparing installation...",
            font=("Segoe UI", 10),
            bg="#f0f0f0",
            fg="#7f8c8d"
        )
        self.status_label.pack()
    
    def update_progress(self, value, status):
        """Update progress bar and status."""
        self.progress_var.set(value)
        self.status_label.config(text=status)
        self.root.update()
    
    def install_portable(self, install_path):
        """Install portable version."""
        self.update_progress(10, "Creating installation directory...")
        
        # Create directory
        install_path.mkdir(parents=True, exist_ok=True)
        
        self.update_progress(20, "Copying application files...")
        
        # Copy files from current directory
        files_to_copy = [
            "GitAccountManagerPro.exe",
            "README.md",
            "RELEASE_NOTES.md",
            "VERSION.txt",
            "run.bat"
        ]
        
        for i, file in enumerate(files_to_copy):
            if Path(file).exists():
                shutil.copy2(file, install_path / file)
                progress = 20 + (i + 1) * 60 // len(files_to_copy)
                self.update_progress(progress, f"Copying {file}...")
        
        self.update_progress(85, "Creating shortcuts...")
        
        # Create desktop shortcut if requested
        if self.create_desktop_shortcut.get():
            self.create_shortcut(
                install_path / "GitAccountManagerPro.exe",
                Path.home() / "Desktop" / "Git Account Manager Pro.lnk",
                "Git Account Manager Pro"
            )
        
        self.update_progress(100, "Installation completed!")
    
    def install_full(self, install_path):
        """Install full version."""
        self.update_progress(10, "Creating installation directory...")
        
        # Create directory
        install_path.mkdir(parents=True, exist_ok=True)
        
        self.update_progress(20, "Copying application files...")
        
        # Copy files
        files_to_copy = [
            "GitAccountManagerPro.exe",
            "README.md",
            "RELEASE_NOTES.md",
            "VERSION.txt"
        ]
        
        for i, file in enumerate(files_to_copy):
            if Path(file).exists():
                shutil.copy2(file, install_path / file)
                progress = 20 + (i + 1) * 50 // len(files_to_copy)
                self.update_progress(progress, f"Copying {file}...")
        
        self.update_progress(70, "Creating shortcuts...")
        
        # Create desktop shortcut
        if self.create_desktop_shortcut.get():
            self.create_shortcut(
                install_path / "GitAccountManagerPro.exe",
                Path.home() / "Desktop" / "Git Account Manager Pro.lnk",
                "Git Account Manager Pro"
            )
        
        # Create start menu shortcut
        if self.create_start_menu.get():
            start_menu = Path.home() / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs"
            start_menu.mkdir(parents=True, exist_ok=True)
            
            self.create_shortcut(
                install_path / "GitAccountManagerPro.exe",
                start_menu / "Git Account Manager Pro.lnk",
                "Git Account Manager Pro"
            )
        
        self.update_progress(90, "Creating uninstaller...")
        
        # Create uninstaller
        self.create_uninstaller(install_path)
        
        self.update_progress(100, "Installation completed!")
    
    def create_shortcut(self, target, shortcut_path, description):
        """Create Windows shortcut."""
        try:
            import winshell
            from win32com.client import Dispatch
            
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(str(shortcut_path))
            shortcut.Targetpath = str(target)
            shortcut.WorkingDirectory = str(target.parent)
            shortcut.Description = description
            shortcut.save()
            
        except ImportError:
            # Fallback: create batch file
            batch_content = f'''@echo off
cd /d "{target.parent}"
"{target}"
'''
            shortcut_path = shortcut_path.with_suffix('.bat')
            with open(shortcut_path, 'w') as f:
                f.write(batch_content)
    
    def create_uninstaller(self, install_path):
        """Create uninstaller script."""
        uninstaller_content = f'''@echo off
echo Uninstalling Git Account Manager Pro...
echo.

REM Remove shortcuts
if exist "%USERPROFILE%\\Desktop\\Git Account Manager Pro.lnk" del "%USERPROFILE%\\Desktop\\Git Account Manager Pro.lnk"
if exist "%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Git Account Manager Pro.lnk" del "%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Git Account Manager Pro.lnk"

REM Remove installation directory
rmdir /s /q "{install_path}"

echo.
echo Git Account Manager Pro has been uninstalled.
pause
'''
        
        with open(install_path / "uninstall.bat", 'w') as f:
            f.write(uninstaller_content)
    
    def show_success(self):
        """Show installation success."""
        # Hide progress UI
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Success UI
        success_frame = tk.Frame(self.root, bg="#f0f0f0")
        success_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Success icon
        tk.Label(
            success_frame,
            text="✅",
            font=("Segoe UI Emoji", 48),
            bg="#f0f0f0"
        ).pack(pady=(0, 20))
        
        # Success message
        tk.Label(
            success_frame,
            text="Installation Completed Successfully!",
            font=("Segoe UI", 18, "bold"),
            bg="#f0f0f0",
            fg="#27ae60"
        ).pack(pady=(0, 10))
        
        # Installation details
        details = f"Installed to: {self.install_path.get()}\n"
        details += f"Type: {'Portable' if self.install_type.get() == 'portable' else 'Full Installation'}\n"
        
        if self.create_desktop_shortcut.get():
            details += "✓ Desktop shortcut created\n"
        if self.create_start_menu.get():
            details += "✓ Start Menu entry created\n"
        
        tk.Label(
            success_frame,
            text=details,
            font=("Segoe UI", 10),
            bg="#f0f0f0",
            fg="#7f8c8d",
            justify="left"
        ).pack(pady=(0, 20))
        
        # Buttons
        button_frame = tk.Frame(success_frame, bg="#f0f0f0")
        button_frame.pack()
        
        # Launch button
        launch_btn = tk.Button(
            button_frame,
            text="Launch Application",
            command=self.launch_app,
            font=("Segoe UI", 11, "bold"),
            bg="#3498db",
            fg="white",
            relief="flat",
            padx=20,
            pady=8
        )
        launch_btn.pack(side="left", padx=(0, 10))
        
        # Close button
        close_btn = tk.Button(
            button_frame,
            text="Close",
            command=self.root.destroy,
            font=("Segoe UI", 11),
            bg="#95a5a6",
            fg="white",
            relief="flat",
            padx=20,
            pady=8
        )
        close_btn.pack(side="left")
    
    def launch_app(self):
        """Launch the installed application."""
        app_path = Path(self.install_path.get()) / "GitAccountManagerPro.exe"
        if app_path.exists():
            subprocess.Popen([str(app_path)])
        self.root.destroy()
    
    def run(self):
        """Run the installer."""
        self.root.mainloop()

def main():
    """Main installer function."""
    print("🚀 Git Account Manager Pro - Installer")
    print("=" * 50)
    
    # Check if running from correct location
    if not Path("GitAccountManagerPro.exe").exists():
        messagebox.showerror(
            "Error",
            "GitAccountManagerPro.exe not found!\n"
            "Please run this installer from the same folder as the application files."
        )
        return 1
    
    # Run installer GUI
    installer = InstallerGUI()
    installer.run()
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
