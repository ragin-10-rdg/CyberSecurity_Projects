#!/usr/bin/env python3
"""
Image Encryption Demo Script
Automated demonstration of image encryption with sample images.
"""

from image_encryption import encrypt_image, decrypt_image, simple_pixel_shift, reverse_pixel_shift
from create_sample_image import create_test_images
import os

def run_demo():
    """Run automated demo of image encryption functionality."""
    print("=" * 60)
    print("       IMAGE ENCRYPTION DEMONSTRATION")
    print("=" * 60)
    
    # Create sample images first
    print("Creating sample images...")
    create_test_images()
    
    # Test cases
    test_images = [
        "sample_images/simple_shapes.png",
        "sample_images/secret_text.png",
        "sample_images/grid_pattern.png"
    ]
    
    print(f"\n1. XOR ENCRYPTION TESTS")
    print("-" * 40)
    
    for i, image_path in enumerate(test_images, 1):
        if os.path.exists(image_path):
            print(f"\nTest {i}: {os.path.basename(image_path)}")
            
            # XOR encryption
            encrypted_path = f"encrypted_{os.path.basename(image_path)}"
            decrypted_path = f"decrypted_{os.path.basename(image_path)}"
            key_seed = 42 + i
            
            success1 = encrypt_image(image_path, encrypted_path, key_seed)
            success2 = decrypt_image(encrypted_path, decrypted_path, key_seed)
            
            print(f"Encryption: {'✓' if success1 else '✗'}")
            print(f"Decryption: {'✓' if success2 else '✗'}")
    
    print(f"\n2. PIXEL SHIFT ENCRYPTION TESTS")
    print("-" * 40)
    
    for i, image_path in enumerate(test_images, 1):
        if os.path.exists(image_path):
            print(f"\nTest {i}: {os.path.basename(image_path)}")
            
            # Pixel shift encryption
            shifted_path = f"shifted_{os.path.basename(image_path)}"
            restored_path = f"restored_{os.path.basename(image_path)}"
            shift_value = 50 + (i * 25)
            
            success1 = simple_pixel_shift(image_path, shifted_path, shift_value)
            success2 = reverse_pixel_shift(shifted_path, restored_path, shift_value)
            
            print(f"Shift Encryption: {'✓' if success1 else '✗'}")
            print(f"Shift Decryption: {'✓' if success2 else '✗'}")
    
    print(f"\nDemo completed! Check the generated encrypted/decrypted images.")

if __name__ == "__main__":
    run_demo()
