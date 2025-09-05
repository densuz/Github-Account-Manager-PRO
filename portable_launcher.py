#!/usr/bin/env python3
"""
Git Account Manager Pro - Portable Launcher
Detects system language and provides portable installation options
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import subprocess
import json
import locale

class PortableLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Git Account Manager Pro - Portable Launcher")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Language detection
        self.detected_language = self.detect_system_language()
        self.selected_language = tk.StringVar(value=self.detected_language)
        
        self.create_ui()
    
    def center_window(self):
        """Center the launcher window."""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.root.winfo_screenheight() // 2) - (400 // 2)
        self.root.geometry(f"500x400+{x}+{y}")
    
    def detect_system_language(self):
        """Detect system language."""
        try:
            # Get system locale
            system_locale = locale.getdefaultlocale()[0]
            
            if system_locale:
                if system_locale.startswith('id'):
                    return 'id'
                elif system_locale.startswith('en'):
                    return 'en'
            
            # Fallback to English
            return 'en'
            
        except:
            return 'en'
    
    def create_ui(self):
        """Create the launcher UI."""
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f8f9fa")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_frame)
        
        # Language selection
        self.create_language_section(main_frame)
        
        # Options
        self.create_options_section(main_frame)
        
        # Buttons
        self.create_buttons(main_frame)
    
    def create_header(self, parent):
        """Create launcher header."""
        header_frame = tk.Frame(parent, bg="#f8f9fa")
        header_frame.pack(fill="x", pady=(0, 20))
        
        # Icon and title
        title_frame = tk.Frame(header_frame, bg="#f8f9fa")
        title_frame.pack()
        
        icon_label = tk.Label(
            title_frame,
            text="🚀",
            font=("Segoe UI Emoji", 32),
            bg="#f8f9fa"
        )
        icon_label.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="Git Account Manager Pro",
            font=("Segoe UI", 18, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50"
        )
        title_label.pack(side="left")
        
        subtitle_label = tk.Label(
            header_frame,
            text="Portable Launcher v2.1.0",
            font=("Segoe UI", 11),
            bg="#f8f9fa",
            fg="#7f8c8d"
        )
        subtitle_label.pack(pady=(10, 0))
    
    def create_language_section(self, parent):
        """Create language selection section."""
        lang_frame = tk.LabelFrame(
            parent,
            text="Language Selection",
            font=("Segoe UI", 12, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            relief="solid",
            bd=1
        )
        lang_frame.pack(fill="x", pady=(0, 20))
        
        # Language container
        lang_container = tk.Frame(lang_frame, bg="#f8f9fa")
        lang_container.pack(fill="x", padx=20, pady=15)
        
        # Language options
        lang_options_frame = tk.Frame(lang_container, bg="#f8f9fa")
        lang_options_frame.pack(fill="x", pady=(0, 10))
        
        # English option
        en_frame = tk.Frame(lang_options_frame, bg="#f8f9fa")
        en_frame.pack(fill="x", pady=(0, 8))
        
        en_radio = tk.Radiobutton(
            en_frame,
            text="🇺🇸 English",
            variable=self.selected_language,
            value="en",
            font=("Segoe UI", 12, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            selectcolor="#f8f9fa",
            activebackground="#f8f9fa",
            activeforeground="#2c3e50"
        )
        en_radio.pack(anchor="w")
        
        # Indonesian option
        id_frame = tk.Frame(lang_options_frame, bg="#f8f9fa")
        id_frame.pack(fill="x", pady=(0, 8))
        
        id_radio = tk.Radiobutton(
            id_frame,
            text="🇮🇩 Bahasa Indonesia",
            variable=self.selected_language,
            value="id",
            font=("Segoe UI", 12, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            selectcolor="#f8f9fa",
            activebackground="#f8f9fa",
            activeforeground="#2c3e50"
        )
        id_radio.pack(anchor="w")
        
        # Detection info
        detected_text = f"Detected system language: {'Bahasa Indonesia' if self.detected_language == 'id' else 'English'}"
        detected_label = tk.Label(
            lang_container,
            text=detected_text,
            font=("Segoe UI", 9),
            bg="#f8f9fa",
            fg="#7f8c8d"
        )
        detected_label.pack(anchor="w", pady=(5, 0))
    
    def create_options_section(self, parent):
        """Create options section."""
        options_frame = tk.LabelFrame(
            parent,
            text="Launch Options",
            font=("Segoe UI", 12, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            relief="solid",
            bd=1
        )
        options_frame.pack(fill="x", pady=(0, 20))
        
        # Options container
        options_container = tk.Frame(options_frame, bg="#f8f9fa")
        options_container.pack(fill="x", padx=20, pady=15)
        
        # Options
        self.create_data_folder = tk.BooleanVar(value=True)
        self.show_console = tk.BooleanVar(value=False)
        self.auto_close = tk.BooleanVar(value=True)
        
        # Create data folder option
        data_frame = tk.Frame(options_container, bg="#f8f9fa")
        data_frame.pack(fill="x", pady=(0, 10))
        
        data_check = tk.Checkbutton(
            data_frame,
            text="Create portable data folder",
            variable=self.create_data_folder,
            font=("Segoe UI", 11, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            selectcolor="#f8f9fa",
            activebackground="#f8f9fa",
            activeforeground="#2c3e50"
        )
        data_check.pack(anchor="w")
        
        data_desc = tk.Label(
            data_frame,
            text="  • Creates 'data' folder for portable settings and configurations",
            font=("Segoe UI", 9),
            bg="#f8f9fa",
            fg="#7f8c8d"
        )
        data_desc.pack(anchor="w", padx=(20, 0))
        
        # Show console option
        console_frame = tk.Frame(options_container, bg="#f8f9fa")
        console_frame.pack(fill="x", pady=(0, 10))
        
        console_check = tk.Checkbutton(
            console_frame,
            text="Show console window",
            variable=self.show_console,
            font=("Segoe UI", 11, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            selectcolor="#f8f9fa",
            activebackground="#f8f9fa",
            activeforeground="#2c3e50"
        )
        console_check.pack(anchor="w")
        
        console_desc = tk.Label(
            console_frame,
            text="  • Useful for debugging and troubleshooting issues",
            font=("Segoe UI", 9),
            bg="#f8f9fa",
            fg="#7f8c8d"
        )
        console_desc.pack(anchor="w", padx=(20, 0))
        
        # Auto close option
        close_frame = tk.Frame(options_container, bg="#f8f9fa")
        close_frame.pack(fill="x", pady=(0, 5))
        
        close_check = tk.Checkbutton(
            close_frame,
            text="Close launcher after starting application",
            variable=self.auto_close,
            font=("Segoe UI", 11, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            selectcolor="#f8f9fa",
            activebackground="#f8f9fa",
            activeforeground="#2c3e50"
        )
        close_check.pack(anchor="w")
        
        close_desc = tk.Label(
            close_frame,
            text="  • Automatically closes this launcher when the application starts",
            font=("Segoe UI", 9),
            bg="#f8f9fa",
            fg="#7f8c8d"
        )
        close_desc.pack(anchor="w", padx=(20, 0))
    
    def create_buttons(self, parent):
        """Create action buttons."""
        button_frame = tk.Frame(parent, bg="#f8f9fa")
        button_frame.pack(fill="x", pady=(20, 0))
        
        # Install button
        install_btn = tk.Button(
            button_frame,
            text="Install Full Version",
            command=self.install_full,
            font=("Segoe UI", 10),
            bg="#3498db",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        install_btn.pack(side="left", padx=(0, 10))
        
        # Launch portable button
        launch_btn = tk.Button(
            button_frame,
            text="Launch Portable",
            command=self.launch_portable,
            font=("Segoe UI", 10, "bold"),
            bg="#27ae60",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        launch_btn.pack(side="left", padx=(0, 10))
        
        # Exit button
        exit_btn = tk.Button(
            button_frame,
            text="Exit",
            command=self.root.destroy,
            font=("Segoe UI", 10),
            bg="#95a5a6",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        exit_btn.pack(side="right")
    
    def install_full(self):
        """Launch full installer."""
        if Path("installer.py").exists():
            try:
                subprocess.Popen([sys.executable, "installer.py"])
                if self.auto_close.get():
                    self.root.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch installer:\n{str(e)}")
        else:
            messagebox.showerror("Error", "Installer not found!\nPlease ensure installer.py is in the same folder.")
    
    def launch_portable(self):
        """Launch portable version."""
        # Set language environment variable
        os.environ['GIT_MANAGER_LANGUAGE'] = self.selected_language.get()
        
        # Create data folder if requested
        if self.create_data_folder.get():
            data_folder = Path("data")
            data_folder.mkdir(exist_ok=True)
            
            # Create language config
            lang_config = {
                "language": self.selected_language.get(),
                "portable": True
            }
            
            with open(data_folder / "language_config.json", 'w', encoding='utf-8') as f:
                json.dump(lang_config, f, indent=2, ensure_ascii=False)
        
        # Launch application
        exe_path = Path("GitAccountManagerPro.exe")
        if exe_path.exists():
            try:
                if self.show_console.get():
                    # Launch with console
                    subprocess.Popen([str(exe_path)], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    # Launch without console
                    subprocess.Popen([str(exe_path)])
                
                if self.auto_close.get():
                    self.root.destroy()
                    
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch application:\n{str(e)}")
        else:
            messagebox.showerror("Error", "GitAccountManagerPro.exe not found!\nPlease ensure the executable is in the same folder.")
    
    def run(self):
        """Run the launcher."""
        self.root.mainloop()

def main():
    """Main launcher function."""
    print("🚀 Git Account Manager Pro - Portable Launcher")
    print("=" * 50)
    
    # Check if running from correct location
    if not Path("GitAccountManagerPro.exe").exists():
        messagebox.showerror(
            "Error",
            "GitAccountManagerPro.exe not found!\n"
            "Please run this launcher from the same folder as the application files."
        )
        return 1
    
    # Run launcher GUI
    launcher = PortableLauncher()
    launcher.run()
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
