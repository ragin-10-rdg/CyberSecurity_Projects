#!/usr/bin/env python3
"""
Caesar Cipher Tool
A simple implementation of the Caesar cipher for educational purposes.
"""

def caesar_encrypt(text, shift):
    """
    Encrypt text using Caesar cipher with given shift value.
    
    Args:
        text (str): The text to encrypt
        shift (int): The shift value (0-25)
    
    Returns:
        str: The encrypted text
    """
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Apply Caesar cipher formula
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def caesar_decrypt(text, shift):
    """
    Decrypt text using Caesar cipher with given shift value.
    
    Args:
        text (str): The text to decrypt
        shift (int): The shift value (0-25)
    
    Returns:
        str: The decrypted text
    """
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)

def brute_force_decrypt(text):
    """
    Try all possible shift values to decrypt the text.
    
    Args:
        text (str): The text to decrypt
    
    Returns:
        dict: Dictionary with shift values as keys and decrypted text as values
    """
    results = {}
    for shift in range(26):
        results[shift] = caesar_decrypt(text, shift)
    return results

def main():
    """Main function to run the Caesar cipher tool."""
    print("=" * 50)
    print("      CAESAR CIPHER TOOL")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Brute force decrypt")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            try:
                shift = int(input("Enter shift value (0-25): "))
                if 0 <= shift <= 25:
                    encrypted = caesar_encrypt(text, shift)
                    print(f"\nOriginal text: {text}")
                    print(f"Encrypted text: {encrypted}")
                else:
                    print("Shift value must be between 0 and 25!")
            except ValueError:
                print("Please enter a valid number for shift value!")
        
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            try:
                shift = int(input("Enter shift value (0-25): "))
                if 0 <= shift <= 25:
                    decrypted = caesar_decrypt(text, shift)
                    print(f"\nEncrypted text: {text}")
                    print(f"Decrypted text: {decrypted}")
                else:
                    print("Shift value must be between 0 and 25!")
            except ValueError:
                print("Please enter a valid number for shift value!")
        
        elif choice == '3':
            text = input("Enter text to brute force decrypt: ")
            results = brute_force_decrypt(text)
            print(f"\nBrute force decryption results for: {text}")
            print("-" * 40)
            for shift, decrypted in results.items():
                print(f"Shift {shift:2d}: {decrypted}")
        
        elif choice == '4':
            print("Thank you for using Caesar Cipher Tool!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
