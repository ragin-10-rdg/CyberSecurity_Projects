#!/usr/bin/env python3
"""
Image Encryption Tool
Encrypt and decrypt images using pixel manipulation with XOR operations.
"""

from PIL import Image
import numpy as np
import os
import sys

def generate_key(size, seed=42):
    """
    Generate a random key for encryption/decryption.
    
    Args:
        size (tuple): Size of the image (width, height)
        seed (int): Random seed for reproducible results
    
    Returns:
        numpy.ndarray: Random key array
    """
    np.random.seed(seed)
    return np.random.randint(0, 256, size, dtype=np.uint8)

def encrypt_image(image_path, output_path, key_seed=42):
    """
    Encrypt an image using XOR operation with a generated key.
    
    Args:
        image_path (str): Path to the input image
        output_path (str): Path to save the encrypted image
        key_seed (int): Seed for key generation
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Open and convert image to RGB
        img = Image.open(image_path).convert('RGB')
        img_array = np.array(img)
        
        # Generate key with same dimensions as image
        key = generate_key(img_array.shape, key_seed)
        
        # Encrypt using XOR operation
        encrypted_array = np.bitwise_xor(img_array, key)
        
        # Save encrypted image
        encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_img.save(output_path)
        
        print(f"Image encrypted successfully: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error encrypting image: {e}")
        return False

def decrypt_image(encrypted_path, output_path, key_seed=42):
    """
    Decrypt an image using XOR operation with the same key.
    
    Args:
        encrypted_path (str): Path to the encrypted image
        output_path (str): Path to save the decrypted image
        key_seed (int): Seed for key generation (must match encryption seed)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Open encrypted image
        encrypted_img = Image.open(encrypted_path).convert('RGB')
        encrypted_array = np.array(encrypted_img)
        
        # Generate the same key used for encryption
        key = generate_key(encrypted_array.shape, key_seed)
        
        # Decrypt using XOR operation (XOR is its own inverse)
        decrypted_array = np.bitwise_xor(encrypted_array, key)
        
        # Save decrypted image
        decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_img.save(output_path)
        
        print(f"Image decrypted successfully: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error decrypting image: {e}")
        return False

def simple_pixel_shift(image_path, output_path, shift_value=50):
    """
    Simple encryption by shifting pixel values.
    
    Args:
        image_path (str): Path to the input image
        output_path (str): Path to save the encrypted image
        shift_value (int): Value to shift pixels by
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        img = Image.open(image_path).convert('RGB')
        img_array = np.array(img)
        
        # Shift pixel values (with wrap-around using modulo)
        shifted_array = (img_array + shift_value) % 256
        
        # Save shifted image
        shifted_img = Image.fromarray(shifted_array.astype('uint8'))
        shifted_img.save(output_path)
        
        print(f"Image encrypted with pixel shift: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error in pixel shift encryption: {e}")
        return False

def reverse_pixel_shift(encrypted_path, output_path, shift_value=50):
    """
    Decrypt image encrypted with pixel shift.
    
    Args:
        encrypted_path (str): Path to the encrypted image
        output_path (str): Path to save the decrypted image
        shift_value (int): Value that was used to shift pixels
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        encrypted_img = Image.open(encrypted_path).convert('RGB')
        encrypted_array = np.array(encrypted_img)
        
        # Reverse the shift
        original_array = (encrypted_array - shift_value) % 256
        
        # Save original image
        original_img = Image.fromarray(original_array.astype('uint8'))
        original_img.save(output_path)
        
        print(f"Image decrypted from pixel shift: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error in pixel shift decryption: {e}")
        return False

def main():
    """Main function to run the image encryption tool."""
    print("=" * 60)
    print("           IMAGE ENCRYPTION TOOL")
    print("=" * 60)
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt image (XOR method)")
        print("2. Decrypt image (XOR method)")
        print("3. Encrypt image (Pixel shift method)")
        print("4. Decrypt image (Pixel shift method)")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            image_path = input("Enter path to image file: ").strip()
            if not os.path.exists(image_path):
                print("Image file not found!")
                continue
            
            output_path = input("Enter output path for encrypted image: ").strip()
            try:
                key_seed = int(input("Enter key seed (integer): "))
                encrypt_image(image_path, output_path, key_seed)
            except ValueError:
                print("Please enter a valid integer for key seed!")
        
        elif choice == '2':
            encrypted_path = input("Enter path to encrypted image: ").strip()
            if not os.path.exists(encrypted_path):
                print("Encrypted image file not found!")
                continue
            
            output_path = input("Enter output path for decrypted image: ").strip()
            try:
                key_seed = int(input("Enter key seed used for encryption: "))
                decrypt_image(encrypted_path, output_path, key_seed)
            except ValueError:
                print("Please enter a valid integer for key seed!")
        
        elif choice == '3':
            image_path = input("Enter path to image file: ").strip()
            if not os.path.exists(image_path):
                print("Image file not found!")
                continue
            
            output_path = input("Enter output path for encrypted image: ").strip()
            try:
                shift_value = int(input("Enter shift value (0-255): "))
                if 0 <= shift_value <= 255:
                    simple_pixel_shift(image_path, output_path, shift_value)
                else:
                    print("Shift value must be between 0 and 255!")
            except ValueError:
                print("Please enter a valid integer for shift value!")
        
        elif choice == '4':
            encrypted_path = input("Enter path to encrypted image: ").strip()
            if not os.path.exists(encrypted_path):
                print("Encrypted image file not found!")
                continue
            
            output_path = input("Enter output path for decrypted image: ").strip()
            try:
                shift_value = int(input("Enter shift value used for encryption: "))
                if 0 <= shift_value <= 255:
                    reverse_pixel_shift(encrypted_path, output_path, shift_value)
                else:
                    print("Shift value must be between 0 and 255!")
            except ValueError:
                print("Please enter a valid integer for shift value!")
        
        elif choice == '5':
            print("Thank you for using Image Encryption Tool!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
