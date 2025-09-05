"""
Reusable UI components for Git Account Manager Pro.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable, Optional, Dict, Any


class UIComponents:
    """Collection of reusable UI components."""
    
    @staticmethod
    def create_styled_button(parent, text: str, command: Callable, 
                           bg_color: str, fg_color: str, hover_color: str,
                           **kwargs) -> tk.Button:
        """
        Create a styled button with hover effects.
        
        Args:
            parent: Parent widget
            text: Button text
            command: Command to execute on click
            bg_color: Background color
            fg_color: Foreground color
            hover_color: Hover background color
            **kwargs: Additional button options
            
        Returns:
            Styled button widget
        """
        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg_color,
            fg=fg_color,
            relief="flat",
            bd=0,
            cursor="hand2",
            **kwargs
        )
        
        # Add hover effects
        def on_enter(e):
            button.config(bg=hover_color)
        
        def on_leave(e):
            button.config(bg=bg_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button
    
    @staticmethod
    def create_styled_entry(parent, **kwargs) -> tk.Entry:
        """
        Create a styled entry widget.
        
        Args:
            parent: Parent widget
            **kwargs: Entry options
            
        Returns:
            Styled entry widget
        """
        default_options = {
            'relief': 'flat',
            'bd': 0,
            'font': ('Segoe UI', 11)
        }
        default_options.update(kwargs)
        
        return tk.Entry(parent, **default_options)
    
    @staticmethod
    def create_styled_label(parent, text: str, **kwargs) -> tk.Label:
        """
        Create a styled label widget.
        
        Args:
            parent: Parent widget
            text: Label text
            **kwargs: Label options
            
        Returns:
            Styled label widget
        """
        default_options = {
            'font': ('Segoe UI', 10),
            'anchor': 'w'
        }
        default_options.update(kwargs)
        
        return tk.Label(parent, text=text, **default_options)
    
    @staticmethod
    def create_tooltip(widget, text: str, theme_colors: Dict[str, str]) -> None:
        """
        Create a tooltip for a widget.
        
        Args:
            widget: Widget to attach tooltip to
            text: Tooltip text
            theme_colors: Theme colors dictionary
        """
        def show_tooltip(event):
            tooltip_window = tk.Toplevel()
            tooltip_window.wm_overrideredirect(True)
            tooltip_window.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            label = tk.Label(
                tooltip_window, 
                text=text, 
                bg=theme_colors["bg_tertiary"], 
                fg=theme_colors["text_primary"], 
                font=("Segoe UI", 8),
                relief="solid", 
                bd=1
            )
            label.pack(padx=5, pady=2)
            widget.tooltip = tooltip_window
        
        def hide_tooltip(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
                del widget.tooltip
        
        widget.bind("<Enter>", show_tooltip)
        widget.bind("<Leave>", hide_tooltip)
    
    @staticmethod
    def create_theme_switcher(parent, current_theme: str, on_theme_change: Callable,
                            theme_colors: Dict[str, str]) -> tk.Frame:
        """
        Create a theme switcher component.
        
        Args:
            parent: Parent widget
            current_theme: Current theme setting
            on_theme_change: Callback for theme changes
            theme_colors: Theme colors dictionary
            
        Returns:
            Theme switcher frame
        """
        theme_frame = tk.Frame(parent, bg=theme_colors["bg_secondary"])
        
        # Theme label
        theme_label = tk.Label(
            theme_frame,
            text="🎨 Tema:",
            font=("Segoe UI", 10, "bold"),
            bg=theme_colors["bg_secondary"],
            fg=theme_colors["text_secondary"]
        )
        theme_label.pack(side="left", padx=(0, 15))
        
        # Theme options
        themes = [
            ("🌙 Dark", "dark", "Dark Mode"),
            ("☀️ Light", "light", "Light Mode"), 
            ("🖥️ System", "system", "Follow System Theme")
        ]
        
        for text, theme_key, tooltip in themes:
            # Create button directly
            is_active = (current_theme == theme_key)
            switch_bg = theme_colors["accent_blue"] if is_active else theme_colors["bg_tertiary"]
            switch_fg = theme_colors["bg_primary"] if is_active else theme_colors["text_secondary"]
            
            btn = tk.Button(
                theme_frame,
                text=text,
                command=lambda t=theme_key: on_theme_change(t),
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
            
            create_hover_effect(btn, switch_bg, theme_colors["hover_blue"])
            
            # Add tooltip
            UIComponents.create_tooltip(btn, tooltip, theme_colors)
        
        return theme_frame
    
    @staticmethod
    def create_scrollable_frame(parent, theme_colors: Dict[str, str]) -> tuple:
        """
        Create a scrollable frame with canvas and scrollbar.
        
        Args:
            parent: Parent widget
            theme_colors: Theme colors dictionary
            
        Returns:
            Tuple of (canvas, scrollable_frame, scrollbar)
        """
        # Canvas dan scrollbar dengan styling modern
        canvas = tk.Canvas(
            parent, 
            bg=theme_colors["bg_primary"], 
            highlightthickness=0, 
            relief="flat"
        )
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=theme_colors["bg_primary"])

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        return canvas, scrollable_frame, scrollbar
    
    @staticmethod
    def show_error_dialog(title: str, message: str) -> None:
        """
        Show error dialog.
        
        Args:
            title: Dialog title
            message: Error message
        """
        messagebox.showerror(title, message)
    
    @staticmethod
    def show_info_dialog(title: str, message: str) -> None:
        """
        Show info dialog.
        
        Args:
            title: Dialog title
            message: Info message
        """
        messagebox.showinfo(title, message)
    
    @staticmethod
    def show_confirm_dialog(title: str, message: str) -> bool:
        """
        Show confirmation dialog.
        
        Args:
            title: Dialog title
            message: Confirmation message
            
        Returns:
            True if confirmed, False otherwise
        """
        return messagebox.askyesno(title, message)
    
    @staticmethod
    def center_window(window, width: int, height: int) -> None:
        """
        Center a window on the screen.
        
        Args:
            window: Window to center
            width: Window width
            height: Window height
        """
        window.update_idletasks()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")
