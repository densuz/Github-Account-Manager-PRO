# Git Account Manager Pro v2.0.0

A professional Git account management tool with modular architecture that allows you to easily manage multiple GitHub accounts and switch between them seamlessly.

## 🚀 Features

- **Multi-Account Management**: Manage multiple GitHub accounts with different credentials
- **One-Click Switching**: Switch between accounts with a single click
- **Automatic Authentication**: Configure personal access tokens for seamless Git operations
- **Modern UI**: Beautiful, responsive interface with dark/light theme support
- **System Theme Detection**: Automatically detects and follows system theme preferences
- **Secure Storage**: Safely stores account credentials locally
- **Token Management**: Show/hide and copy personal access tokens
- **Validation**: Comprehensive input validation for all account data
- **Modular Architecture**: Clean, maintainable code structure

## 📋 Requirements

- **Python 3.6+** (required for f-strings and type hints)
- **Git** (must be installed and accessible from command line)
- **Tkinter** (usually included with Python)
- **Windows 10/11** (for system theme detection) or **Linux/macOS** (basic theme support)

### Optional Dependencies

- **pyperclip** (for enhanced clipboard operations)
  ```bash
  pip install pyperclip
  ```

## 🛠️ Installation

1. **Clone or download** this repository
2. **Ensure Python 3.6+** is installed on your system
3. **Install Git** and ensure it's accessible from command line
4. **Optional**: Install pyperclip for enhanced clipboard support:
   ```bash
   pip install pyperclip
   ```
5. **Run the application**:
   ```bash
   python main.py
   ```

## 🏗️ Project Structure

```
gitswitcher/
├── main.py                 # Main application entry point
├── requirements.txt        # Dependencies and installation info
├── README.md              # This file
├── .gitignore             # Git ignore file for security
├── migrate_to_v2.py       # Migration script (optional)
├── data/                  # 🔒 SECURE DATA DIRECTORY
│   ├── accounts.json      # Account data storage (auto-created)
│   ├── theme_config.json  # Theme preferences (auto-created)
│   └── .git_current_profile # Current active profile (auto-created)
└── src/                   # Source code directory
    ├── __init__.py
    ├── config/            # Configuration and theme management
    │   ├── __init__.py
    │   ├── constants.py   # Application constants and theme definitions
    │   └── settings.py    # Settings and theme management
    ├── core/              # Core business logic
    │   ├── __init__.py
    │   ├── git_manager.py # Git operations and configuration
    │   └── account_manager.py # Account management operations
    ├── ui/                # User interface components
    │   ├── __init__.py
    │   ├── main_window.py # Main application window
    │   ├── account_form.py # Account add/edit form
    │   └── components.py  # Reusable UI components
    └── utils/             # Utility functions and helpers
        ├── __init__.py
        ├── command_runner.py # Command execution utilities
        ├── file_manager.py   # File operations
        └── validators.py     # Input validation
```

## 🎯 Usage

### Adding a New Account

1. Click **"➕ Tambah Akun Baru"** button
2. Fill in the required information:
   - **Name**: Your full name
   - **Email**: Your GitHub email address
   - **Username**: Your GitHub username (optional)
   - **Token**: Personal access token (optional but recommended)
3. Click **"➕ Tambah Akun"** to save

### Switching Between Accounts

1. Find the account you want to activate
2. Click **"🔄 Aktifkan"** button
3. The application will automatically configure Git with the selected account
4. You'll see a success message confirming the switch

### Managing Accounts

- **Edit**: Click the **✏️** button to modify account information
- **Delete**: Click the **🗑️** button to remove an account
- **View Token**: Click the **👁️** button to show/hide the personal access token
- **Copy Token**: Click the **📋** button to copy the token to clipboard

### Theme Management

- **Dark Theme**: Click **"🌙 Dark"** for dark mode
- **Light Theme**: Click **"☀️ Light"** for light mode
- **System Theme**: Click **"🖥️ System"** to follow system preferences

## 🔧 Configuration

### Personal Access Token Setup

To enable automatic authentication, you need to create a GitHub Personal Access Token:

1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Click "Generate new token (classic)"
3. Select appropriate scopes (at minimum: `repo`, `workflow`)
4. Copy the generated token and paste it in the account form

### Git Configuration

The application automatically configures the following Git settings:

- `user.name` and `user.email`
- `github.user` (if username provided)
- `credential.helper` (set to `store`)
- `init.defaultBranch` (set to `main`)
- `pull.rebase` (set to `false`)
- `push.default` (set to `simple`)

## 🏛️ Architecture

The application follows a clean, modular architecture with clear separation of concerns:

- **Configuration Layer** (`src/config/`): Manages themes, settings, and constants
- **Core Layer** (`src/core/`): Contains business logic for Git and account management  
- **UI Layer** (`src/ui/`): Handles user interface components and interactions
- **Utils Layer** (`src/utils/`): Provides utility functions and helpers

## 🔒 Security

- **Secure Data Storage**: All sensitive data is stored in the `data/` directory
- **Local Storage Only**: Account data is stored locally in JSON format
- **Protected Files**: Personal access tokens and account information are secured
- **No External Transmission**: No data is transmitted to external servers
- **Local Git Operations**: All Git operations are performed locally
- **Git Ignore Protection**: The `data/` directory is excluded from version control
- **Automatic Directory Creation**: Secure data directory is created automatically

## 🐛 Troubleshooting

### Common Issues

1. **"Git is not installed" error**:
   - Install Git from [git-scm.com](https://git-scm.com/)
   - Ensure Git is in your system PATH

2. **"Tkinter not available" error**:
   - Install tkinter: `sudo apt-get install python3-tk` (Linux)
   - Or reinstall Python with tkinter support

3. **Token authentication fails**:
   - Verify the token has correct permissions
   - Check if the token has expired
   - Ensure the username matches your GitHub username

4. **Theme not switching**:
   - Restart the application after changing themes
   - Check if theme_config.json is writable

### Debug Mode

Run with verbose output:
```bash
python main.py --verbose
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🆕 Version History

### v2.0.0 (Current)
- Complete modular architecture redesign
- Enhanced theme management
- Improved error handling
- Better code organization
- Comprehensive documentation

### v1.0.0 (Legacy)
- Basic account management
- Simple UI
- Monolithic structure

## 📞 Support

For issues, questions, or contributions, please:
1. Check the troubleshooting section
2. Search existing issues
3. Create a new issue with detailed information

---

**Git Account Manager Pro** - Making Git account management simple and professional! 🚀