#!/usr/bin/env python3
"""
Script to create professional icons for Git Account Manager Pro.
Creates various icon sizes and formats for the application.
"""

import os
from PIL import Image, ImageDraw, ImageFont
import sys

def create_icon(size=256, format='PNG'):
    """Create a professional icon for Git Account Manager Pro."""
    
    # Create a new image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Define colors
    primary_color = (52, 152, 219)  # Blue
    secondary_color = (46, 204, 113)  # Green
    accent_color = (155, 89, 182)  # Purple
    text_color = (255, 255, 255)  # White
    
    # Create gradient background
    for i in range(size):
        # Create a subtle gradient from top to bottom
        alpha = int(255 * (1 - i / size * 0.3))
        color = (primary_color[0], primary_color[1], primary_color[2], alpha)
        draw.line([(0, i), (size, i)], fill=color)
    
    # Draw main circle (Git symbol background)
    circle_radius = int(size * 0.35)
    circle_center = (size // 2, size // 2)
    
    # Draw outer circle with gradient effect
    for r in range(circle_radius, 0, -2):
        alpha = int(255 * (1 - (circle_radius - r) / circle_radius * 0.5))
        color = (secondary_color[0], secondary_color[1], secondary_color[2], alpha)
        draw.ellipse([
            circle_center[0] - r, circle_center[1] - r,
            circle_center[0] + r, circle_center[1] + r
        ], fill=color)
    
    # Draw Git branch symbol
    branch_width = int(size * 0.08)
    branch_length = int(size * 0.25)
    
    # Main branch (vertical)
    draw.rectangle([
        circle_center[0] - branch_width // 2,
        circle_center[1] - branch_length,
        circle_center[0] + branch_width // 2,
        circle_center[1] + branch_length
    ], fill=text_color)
    
    # Left branch (horizontal)
    draw.rectangle([
        circle_center[0] - branch_length,
        circle_center[1] - branch_width // 2,
        circle_center[0] - branch_width,
        circle_center[1] + branch_width // 2
    ], fill=text_color)
    
    # Right branch (horizontal)
    draw.rectangle([
        circle_center[0] + branch_width,
        circle_center[1] - branch_width // 2,
        circle_center[0] + branch_length,
        circle_center[1] + branch_width // 2
    ], fill=text_color)
    
    # Add small circles at branch ends
    circle_size = int(size * 0.06)
    
    # Left circle
    draw.ellipse([
        circle_center[0] - branch_length - circle_size // 2,
        circle_center[1] - circle_size // 2,
        circle_center[0] - branch_length + circle_size // 2,
        circle_center[1] + circle_size // 2
    ], fill=accent_color)
    
    # Right circle
    draw.ellipse([
        circle_center[0] + branch_length - circle_size // 2,
        circle_center[1] - circle_size // 2,
        circle_center[0] + branch_length + circle_size // 2,
        circle_center[1] + circle_size // 2
    ], fill=accent_color)
    
    # Add subtle shadow effect
    shadow_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_img)
    
    # Create shadow
    shadow_offset = int(size * 0.02)
    shadow_draw.ellipse([
        circle_center[0] - circle_radius + shadow_offset,
        circle_center[1] - circle_radius + shadow_offset,
        circle_center[0] + circle_radius + shadow_offset,
        circle_center[1] + circle_radius + shadow_offset
    ], fill=(0, 0, 0, 30))
    
    # Composite shadow with main image
    img = Image.alpha_composite(shadow_img, img)
    
    return img

def create_ico_file():
    """Create ICO file for Windows."""
    sizes = [16, 32, 48, 64, 128, 256]
    images = []
    
    for size in sizes:
        img = create_icon(size)
        images.append(img)
    
    # Save as ICO
    images[0].save('assets/app_icon.ico', format='ICO', sizes=[(img.width, img.height) for img in images])

def create_png_files():
    """Create PNG files in various sizes."""
    sizes = [16, 32, 48, 64, 128, 256, 512]
    
    for size in sizes:
        img = create_icon(size)
        img.save(f'assets/app_icon_{size}x{size}.png', format='PNG')

def create_simple_icon():
    """Create a simpler, more modern icon."""
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Modern flat design colors
    bg_color = (52, 152, 219)  # Blue
    icon_color = (255, 255, 255)  # White
    accent_color = (46, 204, 113)  # Green
    
    # Create rounded rectangle background
    corner_radius = int(size * 0.15)
    draw.rounded_rectangle([
        corner_radius, corner_radius,
        size - corner_radius, size - corner_radius
    ], radius=corner_radius, fill=bg_color)
    
    # Draw Git symbol
    center = size // 2
    symbol_size = int(size * 0.4)
    
    # Main vertical line
    line_width = int(size * 0.08)
    draw.rectangle([
        center - line_width // 2,
        center - symbol_size // 2,
        center + line_width // 2,
        center + symbol_size // 2
    ], fill=icon_color)
    
    # Horizontal lines
    h_line_length = int(symbol_size * 0.6)
    draw.rectangle([
        center - h_line_length,
        center - line_width // 2,
        center - line_width,
        center + line_width // 2
    ], fill=icon_color)
    
    draw.rectangle([
        center + line_width,
        center - line_width // 2,
        center + h_line_length,
        center + line_width // 2
    ], fill=icon_color)
    
    # Add small circles
    circle_size = int(size * 0.08)
    draw.ellipse([
        center - h_line_length - circle_size // 2,
        center - circle_size // 2,
        center - h_line_length + circle_size // 2,
        center + circle_size // 2
    ], fill=accent_color)
    
    draw.ellipse([
        center + h_line_length - circle_size // 2,
        center - circle_size // 2,
        center + h_line_length + circle_size // 2,
        center + circle_size // 2
    ], fill=accent_color)
    
    return img

def main():
    """Main function to create all icon variants."""
    print("🎨 Creating professional icons for Git Account Manager Pro...")
    
    # Create assets directory if it doesn't exist
    os.makedirs('assets', exist_ok=True)
    
    try:
        # Create ICO file for Windows
        print("📱 Creating ICO file...")
        create_ico_file()
        print("✅ app_icon.ico created")
        
        # Create PNG files
        print("🖼️ Creating PNG files...")
        create_png_files()
        print("✅ PNG files created")
        
        # Create simple modern icon
        print("🎯 Creating modern icon...")
        simple_icon = create_simple_icon()
        simple_icon.save('assets/app_icon_modern.png', format='PNG')
        print("✅ Modern icon created")
        
        # Create favicon
        print("🌐 Creating favicon...")
        favicon = create_icon(32)
        favicon.save('assets/favicon.ico', format='ICO')
        print("✅ Favicon created")
        
        print("\n🎉 All icons created successfully!")
        print("📁 Icons saved in assets/ folder:")
        print("   - app_icon.ico (Windows executable icon)")
        print("   - app_icon_modern.png (Modern design)")
        print("   - app_icon_*.png (Various sizes)")
        print("   - favicon.ico (Web favicon)")
        
        return 0
        
    except ImportError:
        print("❌ PIL (Pillow) not installed!")
        print("Please install it with: pip install Pillow")
        return 1
    except Exception as e:
        print(f"❌ Error creating icons: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
