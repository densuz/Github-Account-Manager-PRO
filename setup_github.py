#!/usr/bin/env python3
"""
Script to setup GitHub repository for Git Account Manager Pro.
This script helps prepare the repository for easy user downloads.
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def setup_git_repository():
    """Setup Git repository for GitHub."""
    print("🚀 Setting up Git repository for GitHub...")
    
    # Check if git is available
    if not run_command("git --version", "Checking Git availability"):
        print("❌ Git is not installed or not in PATH")
        return False
    
    # Initialize git if not already initialized
    if not Path(".git").exists():
        if not run_command("git init", "Initializing Git repository"):
            return False
    
    # Add all files
    if not run_command("git add .", "Adding files to Git"):
        return False
    
    # Check if there are changes to commit
    result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if not result.stdout.strip():
        print("ℹ️ No changes to commit")
        return True
    
    # Commit changes
    if not run_command('git commit -m "Setup repository for GitHub distribution"', "Committing changes"):
        return False
    
    print("✅ Git repository setup completed")
    return True

def create_github_instructions():
    """Create instructions for setting up GitHub repository."""
    instructions = """
# 🚀 GitHub Repository Setup Instructions

## 📋 Prerequisites
1. **GitHub Account** - Create account at [github.com](https://github.com)
2. **Git** - Install Git from [git-scm.com](https://git-scm.com)

## 🔧 Setup Steps

### 1. Create GitHub Repository
1. Go to [GitHub](https://github.com)
2. Click **"New repository"**
3. Repository name: `git-account-manager-pro`
4. Description: `Professional Git Account Management Tool`
5. Set to **Public** (for easy downloads)
6. **Don't** initialize with README (we already have one)
7. Click **"Create repository"**

### 2. Connect Local Repository
```bash
# Add remote origin (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/git-account-manager-pro.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Create First Release
1. Go to your repository on GitHub
2. Click **"Releases"** in the sidebar
3. Click **"Create a new release"**
4. Tag version: `v2.1.0`
5. Release title: `Git Account Manager Pro v2.1.0`
6. Upload `GitAccountManagerPro.exe` as asset
7. Add release notes
8. Click **"Publish release"**

### 4. Update Download Links
After creating the release, update these files:
- `README.md` - Replace `your-username` with your GitHub username
- `releases/README.md` - Update download links
- `.github/workflows/build-and-release.yml` - Update repository name

## 🎯 User Download Experience

### Direct Download Link
Users can download directly using:
```
https://github.com/YOUR_USERNAME/git-account-manager-pro/releases/latest/download/GitAccountManagerPro.exe
```

### GitHub Releases Page
Users can browse releases at:
```
https://github.com/YOUR_USERNAME/git-account-manager-pro/releases
```

## 🔄 Automatic Releases (Optional)

The repository includes GitHub Actions workflow for automatic releases:
1. **Push a tag** (e.g., `git tag v2.1.1 && git push origin v2.1.1`)
2. **GitHub Actions** will automatically build and create release
3. **Users** can download from the new release

## 📱 Sharing with Users

### Download Button
Add this to your README:
```markdown
[![Download](https://img.shields.io/badge/Download-GitAccountManagerPro.exe-blue?style=for-the-badge&logo=download)](https://github.com/YOUR_USERNAME/git-account-manager-pro/releases/latest/download/GitAccountManagerPro.exe)
```

### Simple Instructions for Users
1. **Click** the download button
2. **Save** the file to your computer
3. **Double-click** to run (no installation required)
4. **Start** managing your Git accounts!

## 🎉 Benefits

- ✅ **Easy Downloads** - One-click download for users
- ✅ **Version Control** - Track releases and updates
- ✅ **Professional** - Clean, organized repository
- ✅ **Automatic** - GitHub Actions for automated releases
- ✅ **Secure** - GitHub's secure file hosting
- ✅ **Free** - No hosting costs

---
**Your repository is now ready for easy user downloads!** 🚀
"""
    
    with open("GITHUB_SETUP.md", 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✅ GitHub setup instructions created: GITHUB_SETUP.md")

def main():
    """Main function."""
    print("🚀 Git Account Manager Pro - GitHub Setup")
    print("=" * 50)
    
    # Setup git repository
    if not setup_git_repository():
        print("❌ Failed to setup Git repository")
        return 1
    
    # Create GitHub instructions
    create_github_instructions()
    
    print("\n🎉 GitHub setup completed!")
    print("\n📋 Next steps:")
    print("1. Read GITHUB_SETUP.md for detailed instructions")
    print("2. Create GitHub repository")
    print("3. Push your code to GitHub")
    print("4. Create your first release")
    print("5. Share download links with users")
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
