#!/usr/bin/env python3
"""
Create Sample Images for Testing Image Encryption
Generates test images programmatically for demonstration purposes.
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

def create_test_images():
    """Create various test images for encryption testing."""
    
    # Create sample images directory
    os.makedirs("sample_images", exist_ok=True)
    
    # 1. Simple colored rectangle
    img1 = Image.new('RGB', (200, 150), color='red')
    draw = ImageDraw.Draw(img1)
    draw.rectangle([50, 50, 150, 100], fill='blue')
    img1.save("sample_images/simple_shapes.png")
    print("Created: simple_shapes.png")
    
    # 2. Gradient image
    img2 = Image.new('RGB', (256, 256))
    pixels = []
    for y in range(256):
        for x in range(256):
            pixels.append((x, y, (x + y) % 256))
    img2.putdata(pixels)
    img2.save("sample_images/gradient.png")
    print("Created: gradient.png")
    
    # 3. Text image
    img3 = Image.new('RGB', (400, 200), color='white')
    draw = ImageDraw.Draw(img3)
    try:
        # Try to use a default font, fall back to basic if not available
        font = ImageFont.load_default()
    except:
        font = None
    
    draw.text((20, 50), "SECRET MESSAGE", fill='black', font=font)
    draw.text((20, 100), "This is confidential data", fill='red', font=font)
    draw.text((20, 150), "Encrypt me!", fill='blue', font=font)
    img3.save("sample_images/secret_text.png")
    print("Created: secret_text.png")
    
    # 4. Pattern image
    img4 = Image.new('RGB', (300, 300), color='white')
    draw = ImageDraw.Draw(img4)
    for i in range(0, 300, 20):
        draw.line([(i, 0), (i, 300)], fill='black', width=2)
        draw.line([(0, i), (300, i)], fill='black', width=2)
    img4.save("sample_images/grid_pattern.png")
    print("Created: grid_pattern.png")
    
    # 5. Random noise image
    noise_array = np.random.randint(0, 256, (150, 150, 3), dtype=np.uint8)
    img5 = Image.fromarray(noise_array)
    img5.save("sample_images/random_noise.png")
    print("Created: random_noise.png")
    
    print(f"\nAll sample images created in 'sample_images/' directory")

if __name__ == "__main__":
    create_test_images()
