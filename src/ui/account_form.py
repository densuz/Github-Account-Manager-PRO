"""
Account form dialog for Git Account Manager Pro.
"""

import tkinter as tk
from typing import Dict, Any, Optional, Callable

from .components import UIComponents


class AccountForm:
    """Account form dialog for adding/editing accounts."""
    
    def __init__(self, parent, theme_colors: Dict[str, str], 
                 on_save: Callable, on_cancel: Callable,
                 edit_data: Optional[Dict[str, Any]] = None,
                 language_manager=None):
        self.parent = parent
        self.theme_colors = theme_colors
        self.on_save = on_save
        self.on_cancel = on_cancel
        self.edit_data = edit_data
        self.is_edit = edit_data is not None
        self.language_manager = language_manager
        
        self.dialog = None
        self.entries = {}
        
        self.create_dialog()
    
    def translate(self, key: str) -> str:
        """Get translation for a key."""
        if self.language_manager:
            return self.language_manager.translate(key)
        return key
    
    def create_dialog(self) -> None:
        """Create the account form dialog."""
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title(f"✏️ {self.translate('edit_account_title')}" if self.is_edit else f"➕ {self.translate('add_account_title')}")
        self.dialog.geometry("450x550")
        self.dialog.configure(bg=self.theme_colors["bg_primary"])
        self.dialog.resizable(False, False)
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        # Center the dialog
        UIComponents.center_window(self.dialog, 450, 550)
        
        # Main container
        main_frame = tk.Frame(self.dialog, bg=self.theme_colors["bg_primary"])
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.create_header(main_frame)
        self.create_form_fields(main_frame)
        self.create_buttons(main_frame)
        
        # Focus on first field
        self.entries['name'].focus_set()
    
    def create_header(self, parent) -> None:
        """Create dialog header."""
        header_frame = tk.Frame(parent, bg=self.theme_colors["bg_secondary"], relief="flat", bd=0)
        header_frame.pack(fill="x", pady=(0, 20))
        
        header_icon = tk.Label(
            header_frame,
            text="✏️" if self.is_edit else "➕",
            font=("Segoe UI Emoji", 20),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_primary"]
        )
        header_icon.pack(pady=15)
        
        header_title = tk.Label(
            header_frame,
            text="Edit Akun GitHub" if self.is_edit else "Tambah Akun GitHub Baru",
            font=("Segoe UI", 16, "bold"),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_primary"]
        )
        header_title.pack()
        
        header_subtitle = tk.Label(
            header_frame,
            text="Perbarui informasi akun" if self.is_edit else "Masukkan informasi akun GitHub Anda",
            font=("Segoe UI", 10),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_secondary"]
        )
        header_subtitle.pack(pady=(5, 15))
    
    def create_form_fields(self, parent) -> None:
        """Create form input fields."""
        fields_frame = tk.Frame(parent, bg=self.theme_colors["bg_primary"])
        fields_frame.pack(fill="x", pady=(0, 20))
        
        # Name field
        self.create_field(
            fields_frame, 
            "name", 
            "👤 Nama Lengkap *", 
            self.edit_data.get("name", "") if self.is_edit else ""
        )
        
        # Email field
        self.create_field(
            fields_frame, 
            "email", 
            "📧 Email *", 
            self.edit_data.get("email", "") if self.is_edit else ""
        )
        
        # Username field
        self.create_field(
            fields_frame, 
            "username", 
            "🐙 Username GitHub (opsional)", 
            self.edit_data.get("username", "") if self.is_edit else ""
        )
        
        # Token field
        self.create_token_field(fields_frame)
    
    def create_field(self, parent, field_name: str, label_text: str, default_value: str = "") -> None:
        """Create a form field with label and entry."""
        label = UIComponents.create_styled_label(
            parent,
            label_text,
            font=("Segoe UI", 10, "bold"),
            bg=self.theme_colors["bg_primary"],
            fg=self.theme_colors["text_primary"]
        )
        label.pack(fill="x", pady=(0, 5))
        
        entry = UIComponents.create_styled_entry(
            parent,
            font=("Segoe UI", 11),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_primary"],
            insertbackground=self.theme_colors["text_primary"]
        )
        entry.pack(fill="x", ipady=8, pady=(0, 15))
        
        if default_value:
            entry.insert(0, default_value)
        
        self.entries[field_name] = entry
    
    def create_token_field(self, parent) -> None:
        """Create token field with special handling."""
        label = UIComponents.create_styled_label(
            parent,
            "🔑 Personal Access Token (opsional)",
            font=("Segoe UI", 10, "bold"),
            bg=self.theme_colors["bg_primary"],
            fg=self.theme_colors["text_primary"]
        )
        label.pack(fill="x", pady=(0, 5))
        
        entry = UIComponents.create_styled_entry(
            parent,
            font=("Segoe UI", 11),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_primary"],
            show="*",
            insertbackground=self.theme_colors["text_primary"]
        )
        entry.pack(fill="x", ipady=8, pady=(0, 10))
        
        if self.is_edit and self.edit_data.get("token"):
            entry.insert(0, self.edit_data["token"])
        
        self.entries['token'] = entry
        
        # Token info
        token_info = tk.Label(
            parent,
            text="💡 Token diperlukan untuk otentikasi Git otomatis",
            font=("Segoe UI", 9),
            bg=self.theme_colors["bg_primary"],
            fg=self.theme_colors["text_muted"],
            anchor="w"
        )
        token_info.pack(fill="x", pady=(0, 20))
    
    def create_buttons(self, parent) -> None:
        """Create dialog buttons."""
        button_frame = tk.Frame(parent, bg=self.theme_colors["bg_primary"])
        button_frame.pack(fill="x")
        
        # Save button
        save_btn = UIComponents.create_styled_button(
            button_frame,
            text="💾 Simpan" if self.is_edit else "➕ Tambah Akun",
            command=self.save_account,
            bg_color=self.theme_colors["accent_green"],
            fg_color=self.theme_colors["bg_primary"],
            hover_color=self.theme_colors["hover_green"],
            font=("Segoe UI", 11, "bold"),
            padx=30,
            pady=10
        )
        save_btn.pack(side="right", padx=(10, 0))
        
        # Cancel button
        cancel_btn = UIComponents.create_styled_button(
            button_frame,
            text="❌ Batal",
            command=self.cancel,
            bg_color=self.theme_colors["accent_red"],
            fg_color=self.theme_colors["bg_primary"],
            hover_color=self.theme_colors["hover_red"],
            font=("Segoe UI", 11, "bold"),
            padx=30,
            pady=10
        )
        cancel_btn.pack(side="right")
    
    def save_account(self) -> None:
        """Handle save button click."""
        # Get form data
        form_data = {}
        for field_name, entry in self.entries.items():
            value = entry.get().strip()
            if value:  # Only include non-empty values
                form_data[field_name] = value
        
        # Validate required fields
        if not form_data.get('name') or not form_data.get('email'):
            UIComponents.show_error_dialog("Error", "Nama dan Email wajib diisi!")
            return
        
        # Call save callback
        self.on_save(form_data, self.edit_data.get('key') if self.is_edit else None)
        self.dialog.destroy()
    
    def cancel(self) -> None:
        """Handle cancel button click."""
        self.on_cancel()
        self.dialog.destroy()
