"""
Main window for Git Account Manager Pro.
"""

import os
import tkinter as tk
from tkinter import ttk
from typing import Dict, Any, Optional

from ..core.git_manager import GitManager
from ..core.account_manager import AccountManager
from ..config.settings import ConfigManager
from .components import UIComponents
from .account_form import AccountForm


class MainWindow:
    """Main application window."""
    
    def __init__(self):
        self.root = None
        self.frame = None
        
        # Initialize managers
        self.config_manager = ConfigManager()
        self.git_manager = GitManager()
        self.account_manager = AccountManager()
        
        # Initialize configuration
        self.config_manager.initialize()
        self.theme_colors = self.config_manager.get_theme_manager().get_theme_colors()
        self.language_manager = self.config_manager.get_language_manager()
        
        self.create_window()
    
    def create_window(self) -> None:
        """Create the main application window."""
        try:
            self.root = tk.Tk()
            self.root.title("🔐 Git Account Manager Pro")
            self.root.geometry("650x600")
            self.root.configure(bg=self.theme_colors["bg_primary"])
            self.root.resizable(True, True)
            
            # Set application icon
            try:
                icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'app_icon.ico')
                if os.path.exists(icon_path):
                    self.root.iconbitmap(icon_path)
            except Exception:
                pass  # Icon setting is optional
            
            # Set minimum size
            self.root.minsize(600, 500)
            
            # Handle window closing
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            
            self.create_ui()
            self.refresh_ui()
            
        except Exception as e:
            print(f"Error creating window: {e}")
            UIComponents.show_error_dialog("Error", f"Gagal membuat GUI:\n{e}")
    
    def create_ui(self) -> None:
        """Create the main UI components."""
        # Main container
        main_container = tk.Frame(self.root, bg=self.theme_colors["bg_primary"])
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Create header
        self.create_header(main_container)
        
        # Create content area
        self.create_content_area(main_container)
        
        # Create button container
        self.create_button_container(main_container)
    
    def create_header(self, parent) -> None:
        """Create application header."""
        header_frame = tk.Frame(parent, bg=self.theme_colors["bg_secondary"], relief="flat", bd=0)
        header_frame.pack(fill="x", pady=(0, 20))
        
        # Icon dan title
        title_frame = tk.Frame(header_frame, bg=self.theme_colors["bg_secondary"])
        title_frame.pack(pady=20)
        
        # Try to load professional icon, fallback to emoji
        try:
            icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'app_icon_64x64.png')
            if os.path.exists(icon_path):
                # Load and display the professional icon
                from PIL import Image, ImageTk
                icon_img = Image.open(icon_path)
                icon_photo = ImageTk.PhotoImage(icon_img)
                header_icon = tk.Label(
                    title_frame,
                    image=icon_photo,
                    bg=self.theme_colors["bg_secondary"]
                )
                header_icon.image = icon_photo  # Keep a reference
            else:
                raise FileNotFoundError("Icon not found")
        except Exception:
            # Fallback to emoji if icon loading fails
            header_icon = tk.Label(
                title_frame,
                text="🔐",
                font=("Segoe UI Emoji", 24),
                bg=self.theme_colors["bg_secondary"],
                fg=self.theme_colors["text_primary"]
            )
        
        header_icon.pack(side="left", padx=(0, 10))
        
        header = tk.Label(
            title_frame,
            text=self.language_manager.translate("app_title"),
            font=("Segoe UI", 20, "bold"),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_primary"]
        )
        header.pack(side="left")
        
        # Subtitle
        subtitle = tk.Label(
            header_frame,
            text=self.language_manager.translate("app_subtitle"),
            font=("Segoe UI", 10),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_secondary"]
        )
        subtitle.pack(pady=(0, 10))
        
        # Theme and language switchers - create directly in header
        self.create_theme_switcher_simple(header_frame)
        self.create_language_switcher_simple(header_frame)
    
    def create_theme_switcher_simple(self, parent) -> None:
        """Create simple theme switcher component."""
        # Create theme frame
        theme_frame = tk.Frame(parent, bg=self.theme_colors["bg_secondary"])
        theme_frame.pack(pady=(0, 15))
        
        # Theme label
        theme_label = tk.Label(
            theme_frame,
            text="🎨 Tema:",
            font=("Segoe UI", 10, "bold"),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_secondary"]
        )
        theme_label.pack(side="left", padx=(0, 15))
        
        # Theme buttons - simple implementation
        dark_btn = tk.Button(
            theme_frame,
            text="🌙 Dark",
            command=lambda: self.switch_theme("dark"),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            bd=0,
            font=("Segoe UI", 9, "bold"),
            padx=12,
            pady=6,
            cursor="hand2"
        )
        dark_btn.pack(side="left", padx=(0, 12))
        
        light_btn = tk.Button(
            theme_frame,
            text="☀️ Light",
            command=lambda: self.switch_theme("light"),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            bd=0,
            font=("Segoe UI", 9, "bold"),
            padx=12,
            pady=6,
            cursor="hand2"
        )
        light_btn.pack(side="left", padx=(0, 12))
        
        system_btn = tk.Button(
            theme_frame,
            text="🖥️ System",
            command=lambda: self.switch_theme("system"),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            bd=0,
            font=("Segoe UI", 9, "bold"),
            padx=12,
            pady=6,
            cursor="hand2"
        )
        system_btn.pack(side="left", padx=(0, 12))
        
        print("🎨 Theme switcher buttons created successfully!")
    
    def create_language_switcher_simple(self, parent) -> None:
        """Create simple language switcher component."""
        # Create language frame
        language_frame = tk.Frame(parent, bg=self.theme_colors["bg_secondary"])
        language_frame.pack(pady=(0, 15))
        
        # Language label
        language_label = tk.Label(
            language_frame,
            text="🌐 Bahasa:",
            font=("Segoe UI", 10, "bold"),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_secondary"]
        )
        language_label.pack(side="left", padx=(0, 15))
        
        # Language buttons - simple implementation
        current_lang = self.language_manager.get_current_language()
        
        en_btn = tk.Button(
            language_frame,
            text="🇺🇸 English",
            command=lambda: self.switch_language("en"),
            bg="#89b4fa" if current_lang == "en" else self.theme_colors["bg_tertiary"],
            fg="#1e1e2e" if current_lang == "en" else self.theme_colors["text_secondary"],
            relief="flat",
            bd=0,
            font=("Segoe UI", 9, "bold"),
            padx=12,
            pady=6,
            cursor="hand2"
        )
        en_btn.pack(side="left", padx=(0, 12))
        
        id_btn = tk.Button(
            language_frame,
            text="🇮🇩 Bahasa Indonesia",
            command=lambda: self.switch_language("id"),
            bg="#89b4fa" if current_lang == "id" else self.theme_colors["bg_tertiary"],
            fg="#1e1e2e" if current_lang == "id" else self.theme_colors["text_secondary"],
            relief="flat",
            bd=0,
            font=("Segoe UI", 9, "bold"),
            padx=12,
            pady=6,
            cursor="hand2"
        )
        id_btn.pack(side="left", padx=(0, 12))
        
        print("🌐 Language switcher buttons created successfully!")
    
    def create_theme_switcher_direct(self, parent) -> None:
        """Create theme switcher component directly."""
        current_theme_setting = "system"  # default
        try:
            from ..config.constants import CONFIG_FILES
            import json
            import os
            if os.path.exists(CONFIG_FILES['theme_config']):
                with open(CONFIG_FILES['theme_config'], 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    current_theme_setting = config.get("theme", "system")
        except:
            pass
        
        # Create theme frame
        theme_frame = tk.Frame(parent, bg=self.theme_colors["bg_secondary"])
        theme_frame.pack(pady=(0, 15))
        
        # Theme label
        theme_label = tk.Label(
            theme_frame,
            text="🎨 Tema:",
            font=("Segoe UI", 10, "bold"),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_secondary"]
        )
        theme_label.pack(side="left", padx=(0, 15))
        
        # Theme buttons
        themes = [
            ("🌙 Dark", "dark"),
            ("☀️ Light", "light"), 
            ("🖥️ System", "system")
        ]
        
        for text, theme_key in themes:
            is_active = (current_theme_setting == theme_key)
            switch_bg = self.theme_colors["accent_blue"] if is_active else self.theme_colors["bg_tertiary"]
            switch_fg = self.theme_colors["bg_primary"] if is_active else self.theme_colors["text_secondary"]
            
            btn = tk.Button(
                theme_frame,
                text=text,
                command=lambda t=theme_key: self.switch_theme(t),
                bg=switch_bg,
                fg=switch_fg,
                relief="flat",
                bd=0,
                font=("Segoe UI", 9, "bold"),
                padx=12,
                pady=6,
                cursor="hand2"
            )
            btn.pack(side="left", padx=(0, 12))
            
            # Add hover effects
            def create_hover_effect(button, normal_color, hover_color):
                def on_enter(e):
                    button.config(bg=hover_color)
                def on_leave(e):
                    button.config(bg=normal_color)
                button.bind("<Enter>", on_enter)
                button.bind("<Leave>", on_leave)
            
            create_hover_effect(btn, switch_bg, self.theme_colors["hover_blue"])
    
    def create_theme_switcher(self, parent) -> None:
        """Create theme switcher component."""
        current_theme_setting = "system"  # default
        try:
            from ..config.constants import CONFIG_FILES
            import json
            import os
            if os.path.exists(CONFIG_FILES['theme_config']):
                with open(CONFIG_FILES['theme_config'], 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    current_theme_setting = config.get("theme", "system")
        except:
            pass
        
        # Create theme switcher directly in parent
        UIComponents.create_theme_switcher(
            parent,
            current_theme_setting,
            self.switch_theme,
            self.theme_colors
        )
    
    def create_content_area(self, parent) -> None:
        """Create content area with scrollable accounts list."""
        content_frame = tk.Frame(parent, bg=self.theme_colors["bg_secondary"], relief="flat", bd=0)
        content_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        # Label untuk section
        accounts_label = tk.Label(
            content_frame,
            text=f"📋 {self.language_manager.translate('accounts_list')}",
            font=("Segoe UI", 12, "bold"),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_primary"],
            anchor="w"
        )
        accounts_label.pack(fill="x", padx=20, pady=(15, 10))
        
        # Frame untuk scrollable area
        scroll_container = tk.Frame(content_frame, bg=self.theme_colors["bg_secondary"])
        scroll_container.pack(fill="both", expand=True, padx=20, pady=(0, 15))
        
        # Create scrollable frame
        canvas, scrollable_frame, scrollbar = UIComponents.create_scrollable_frame(
            scroll_container, self.theme_colors
        )
        
        self.frame = scrollable_frame
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_button_container(self, parent) -> None:
        """Create button container."""
        button_container = tk.Frame(parent, bg=self.theme_colors["bg_primary"])
        button_container.pack(fill="x")
        
        # Add account button
        btn_add = UIComponents.create_styled_button(
            button_container,
            text=f"➕ {self.language_manager.translate('add_account')}",
            command=self.add_account,
            bg_color=self.theme_colors["accent_blue"],
            fg_color=self.theme_colors["bg_primary"],
            hover_color=self.theme_colors["hover_blue"],
            font=("Segoe UI", 11, "bold"),
            padx=30,
            pady=12
        )
        btn_add.pack(pady=10)
    
    def switch_theme(self, theme_name: str) -> None:
        """Handle theme switching."""
        self.config_manager.get_theme_manager().apply_theme(theme_name)
        # Restart the application to apply new theme
        self.root.destroy()
        self.__init__()
    
    def switch_language(self, language_code: str) -> None:
        """Handle language switching."""
        self.language_manager.set_language(language_code)
        # Restart the application to apply new language
        self.root.destroy()
        self.__init__()
    
    def add_account(self) -> None:
        """Show add account form."""
        AccountForm(
            self.root,
            self.theme_colors,
            self.save_account,
            self.cancel_account_form,
            language_manager=self.language_manager
        )
    
    def edit_account(self, account_key: str) -> None:
        """Show edit account form."""
        account_data = self.account_manager.get_account(account_key)
        if not account_data:
            UIComponents.show_error_dialog(self.language_manager.translate('error'), self.language_manager.translate('account_not_found'))
            return
        
        # Add key to data for editing
        edit_data = account_data.copy()
        edit_data['key'] = account_key
        
        AccountForm(
            self.root,
            self.theme_colors,
            self.save_account,
            self.cancel_account_form,
            edit_data,
            language_manager=self.language_manager
        )
    
    def save_account(self, form_data: Dict[str, Any], account_key: Optional[str] = None) -> None:
        """Handle account save."""
        if account_key:
            # Update existing account
            success, message = self.account_manager.update_account(account_key, form_data)
        else:
            # Add new account
            success, message, new_key = self.account_manager.add_account(form_data)
        
        if success:
            UIComponents.show_info_dialog(f"✅ {self.language_manager.translate('success')}", message)
            self.refresh_ui()
        else:
            UIComponents.show_error_dialog(self.language_manager.translate('error'), message)
    
    def cancel_account_form(self) -> None:
        """Handle account form cancellation."""
        pass  # Nothing to do on cancel
    
    def confirm_delete_account(self, account_key: str) -> None:
        """Show delete confirmation dialog."""
        account_data = self.account_manager.get_account(account_key)
        if not account_data:
            return
        
        result = UIComponents.show_confirm_dialog(
            f"⚠️ {self.language_manager.translate('confirm_delete')}", 
            f"{self.language_manager.translate('confirm_delete_message')}\n\n"
            f"👤 {self.language_manager.translate('name')}: {account_data['name']}\n"
            f"📧 {self.language_manager.translate('email')}: {account_data['email']}\n\n"
            f"⚠️ {self.language_manager.translate('action_cannot_undo')}"
        )
        
        if result:
            self.delete_account(account_key)
    
    def delete_account(self, account_key: str) -> None:
        """Delete an account."""
        success, message = self.account_manager.delete_account(account_key)
        if success:
            UIComponents.show_info_dialog(f"✅ {self.language_manager.translate('success')}", message)
            self.refresh_ui()
        else:
            UIComponents.show_error_dialog(self.language_manager.translate('error'), message)
    
    def switch_to_account(self, account_key: str, account_data: Dict[str, Any]) -> None:
        """Switch to a specific account."""
        try:
            self.git_manager.switch_to_account(account_key, account_data)
            
            # Show success message
            success_msg = f"✅ {self.language_manager.translate('account_switched_success')}\n\n"
            success_msg += f"👤 {self.language_manager.translate('name')}: {account_data['name']}\n"
            success_msg += f"📧 {self.language_manager.translate('email')}: {account_data['email']}\n"
            
            if "username" in account_data and account_data["username"]:
                success_msg += f"🐙 GitHub: @{account_data['username']}\n"
            
            if "token" in account_data and account_data["token"]:
                success_msg += f"🔑 {self.language_manager.translate('token_configured')}\n"
                success_msg += f"🚀 {self.language_manager.translate('ready_for_git')}"
            else:
                success_msg += f"⚠️ {self.language_manager.translate('no_token_warning')}"
            
            UIComponents.show_info_dialog(f"✅ {self.language_manager.translate('account_switched')}", success_msg)
            self.refresh_ui()
            
        except Exception as e:
            error_msg = f"❌ {self.language_manager.translate('failed_to_switch')}:\n{str(e)}"
            print(error_msg)
            UIComponents.show_error_dialog(f"❌ {self.language_manager.translate('switch_failed')}", error_msg)
    
    def refresh_ui(self) -> None:
        """Refresh the UI with current account data."""
        try:
            if not self.frame:
                return
            
            # Clear existing widgets
            for widget in self.frame.winfo_children():
                widget.destroy()
            
            # Sync current profile
            current_profile = self.git_manager.sync_current_profile()
            if current_profile is None:
                current_profile = self.account_manager.get_current_profile()
            
            # Load accounts
            accounts = self.account_manager.load_accounts()
            
            if not accounts:
                self.show_empty_state()
                return
            
            # Display accounts
            for acc_key, data in accounts.items():
                self.create_account_card(acc_key, data, acc_key == current_profile)
                
        except Exception as e:
            print(f"Error in refresh_ui: {e}")
    
    def show_empty_state(self) -> None:
        """Show empty state when no accounts exist."""
        empty_frame = tk.Frame(self.frame, bg=self.theme_colors["bg_primary"])
        empty_frame.pack(pady=40, fill='x')
        
        empty_icon = tk.Label(
            empty_frame,
            text="📝",
            font=("Segoe UI Emoji", 32),
            bg=self.theme_colors["bg_primary"],
            fg=self.theme_colors["text_muted"]
        )
        empty_icon.pack()
        
        empty_label = tk.Label(
            empty_frame,
            text=self.language_manager.translate("no_accounts"),
            font=("Segoe UI", 14, "bold"),
            bg=self.theme_colors["bg_primary"],
            fg=self.theme_colors["text_muted"]
        )
        empty_label.pack(pady=(10, 5))
        
        empty_desc = tk.Label(
            empty_frame,
            text=self.language_manager.translate("no_accounts_desc"),
            font=("Segoe UI", 10),
            bg=self.theme_colors["bg_primary"],
            fg=self.theme_colors["text_muted"]
        )
        empty_desc.pack()
    
    def create_account_card(self, acc_key: str, data: Dict[str, Any], is_active: bool) -> None:
        """Create an account card widget."""
        # Card container
        card_frame = tk.Frame(self.frame, bg=self.theme_colors["bg_secondary"], relief="flat", bd=0)
        card_frame.pack(pady=8, fill='x', padx=15)
        
        # Inner card
        inner_card = tk.Frame(card_frame, bg=self.theme_colors["bg_secondary"])
        inner_card.pack(fill='x', padx=2, pady=2)
        
        # Main button area
        btn_container = tk.Frame(inner_card, bg=self.theme_colors["bg_secondary"])
        btn_container.pack(fill='x', pady=10, padx=15)
        
        # Account info
        self.create_account_info(btn_container, data, is_active)
        
        # Action buttons
        self.create_account_actions(btn_container, acc_key, data, is_active)
    
    def create_account_info(self, parent, data: Dict[str, Any], is_active: bool) -> None:
        """Create account information display."""
        info_frame = tk.Frame(parent, bg=self.theme_colors["bg_secondary"])
        info_frame.pack(fill='x')
        
        # Status badge
        status_color = self.theme_colors["accent_green"] if is_active else self.theme_colors["text_muted"]
        status_text = f"🟢 {self.language_manager.translate('status_active')}" if is_active else f"⚪ {self.language_manager.translate('status_inactive')}"
        
        status_label = tk.Label(
            info_frame,
            text=status_text,
            font=("Segoe UI", 8, "bold"),
            bg=self.theme_colors["bg_secondary"],
            fg=status_color
        )
        status_label.pack(anchor="w")
        
        # Name and email
        name_label = tk.Label(
            info_frame,
            text=data['name'],
            font=("Segoe UI", 12, "bold"),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_primary"],
            anchor="w"
        )
        name_label.pack(anchor="w", pady=(5, 2))
        
        email_label = tk.Label(
            info_frame,
            text=f"📧 {data['email']}",
            font=("Segoe UI", 9),
            bg=self.theme_colors["bg_secondary"],
            fg=self.theme_colors["text_secondary"],
            anchor="w"
        )
        email_label.pack(anchor="w")
        
        # Additional details
        self.create_account_details(info_frame, data)
    
    def create_account_details(self, parent, data: Dict[str, Any]) -> None:
        """Create account details (username, token info)."""
        details_frame = tk.Frame(parent, bg="#313244")
        details_frame.pack(anchor="w", pady=(5, 0))
        
        if data.get('username'):
            username_label = tk.Label(
                details_frame,
                text=f"👤 @{data['username']}",
                font=("Segoe UI", 9),
                bg="#313244",
                fg="#89b4fa"
            )
            username_label.pack(side="left", padx=(0, 15))
        
        if data.get('token'):
            self.create_token_display(details_frame, data['token'])
    
    def create_token_display(self, parent, token: str) -> None:
        """Create token display with show/hide functionality."""
        token_frame = tk.Frame(parent, bg="#313244")
        token_frame.pack(side="left", fill="x")
        
        token_display_frame = tk.Frame(token_frame, bg="#313244")
        token_display_frame.pack(anchor="w", pady=(2, 0))
        
        token_icon = tk.Label(
            token_display_frame,
            text="🔑",
            font=("Segoe UI", 9),
            bg="#313244",
            fg="#a6e3a1"
        )
        token_icon.pack(side="left")
        
        # Token visibility state
        token_visible = tk.BooleanVar(value=False)
        
        def get_display_token():
            if token_visible.get():
                return token
            else:
                return "*" * min(len(token), 20)
        
        token_text = tk.Label(
            token_display_frame,
            text=get_display_token(),
            font=("Segoe UI", 9, "bold"),
            bg="#313244",
            fg="#a6e3a1",
            anchor="w"
        )
        token_text.pack(side="left", padx=(5, 10))
        
        # Show/hide button
        def toggle_token_visibility():
            token_visible.set(not token_visible.get())
            token_text.config(text=get_display_token())
            show_btn.config(text="👁️" if not token_visible.get() else "🙈")
        
        show_btn = tk.Button(
            token_display_frame,
            text="👁️",
            font=("Segoe UI", 8),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            bd=0,
            width=3,
            height=1,
            cursor="hand2",
            command=toggle_token_visibility
        )
        show_btn.pack(side="left", padx=(0, 5))
        
        # Copy button
        def copy_token():
            try:
                import pyperclip
                pyperclip.copy(token)
                copy_btn.config(text="✅", bg="#a6e3a1")
                copy_btn.after(1000, lambda: copy_btn.config(text="📋", bg="#f9e2af"))
            except ImportError:
                copy_btn.clipboard_clear()
                copy_btn.clipboard_append(token)
                copy_btn.update()
                copy_btn.config(text="✅", bg="#a6e3a1")
                copy_btn.after(1000, lambda: copy_btn.config(text="📋", bg="#f9e2af"))
            except Exception as e:
                UIComponents.show_info_dialog("Token", f"Token: {token}")
        
        copy_btn = tk.Button(
            token_display_frame,
            text="📋",
            font=("Segoe UI", 8),
            bg="#f9e2af",
            fg="#1e1e2e",
            relief="flat",
            bd=0,
            width=3,
            height=1,
            cursor="hand2",
            command=copy_token
        )
        copy_btn.pack(side="left")
    
    def create_account_actions(self, parent, acc_key: str, data: Dict[str, Any], is_active: bool) -> None:
        """Create account action buttons."""
        button_area = tk.Frame(parent, bg="#313244")
        button_area.pack(fill='x', pady=(15, 0))
        
        # Switch button
        left_button_frame = tk.Frame(button_area, bg="#313244")
        left_button_frame.pack(side="left", fill="x", expand=True)
        
        switch_btn = UIComponents.create_styled_button(
            left_button_frame,
            text=f"🔄 {self.language_manager.translate('activate')}" if not is_active else f"✅ {self.language_manager.translate('currently_active')}",
            command=lambda: self.switch_to_account(acc_key, data) if not is_active else None,
            bg_color="#89b4fa" if not is_active else "#a6e3a1",
            fg_color="#1e1e2e",
            hover_color="#74c0fc" if not is_active else "#94d3a2",
            font=("Segoe UI", 9, "bold"),
            padx=25,
            pady=10
        )
        switch_btn.pack(side="left", anchor="w")
        
        # Action buttons
        action_frame = tk.Frame(button_area, bg="#313244")
        action_frame.pack(side="right", padx=(20, 0))
        
        # Edit button
        edit_btn = UIComponents.create_styled_button(
            action_frame,
            text="✏️",
            command=lambda: self.edit_account(acc_key),
            bg_color="#f9e2af",
            fg_color="#1e1e2e",
            hover_color="#f5d76e",
            font=("Segoe UI", 12),
            width=4,
            height=1
        )
        edit_btn.pack(side="left", padx=(0, 10))
        
        # Delete button
        delete_btn = UIComponents.create_styled_button(
            action_frame,
            text="🗑️",
            command=lambda: self.confirm_delete_account(acc_key),
            bg_color="#f38ba8",
            fg_color="#1e1e2e",
            hover_color="#f06292",
            font=("Segoe UI", 12),
            width=4,
            height=1
        )
        delete_btn.pack(side="left", padx=(0, 5))
    
    def on_closing(self) -> None:
        """Handle window closing."""
        try:
            self.root.quit()
            self.root.destroy()
        except:
            pass
    
    def run(self) -> None:
        """Run the application."""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nAplikasi dihentikan oleh pengguna")
            self.on_closing()
        except Exception as e:
            print(f"Error dalam mainloop: {e}")
            self.on_closing()
