#!/usr/bin/env python3
"""
Caesar Cipher Demo Script
Automated demonstration of the Caesar cipher tool with test data.
"""

from caesar_cipher import caesar_encrypt, caesar_decrypt, brute_force_decrypt

def run_demo():
    """Run automated demo of Caesar cipher functionality."""
    print("=" * 60)
    print("         CAESAR CIPHER DEMONSTRATION")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ("Hello World!", 3),
        ("The Quick Brown Fox", 5),
        ("Password123! @#$%", 7),
        ("CLASSIFIED INFO", 15),
        ("cybersecurity", 8)
    ]
    
    print("\n1. ENCRYPTION/DECRYPTION TESTS")
    print("-" * 40)
    
    for i, (message, shift) in enumerate(test_cases, 1):
        encrypted = caesar_encrypt(message, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        
        print(f"\nTest {i}:")
        print(f"Original:  {message}")
        print(f"Shift {shift:2d}:   {encrypted}")
        print(f"Decrypted: {decrypted}")
        print(f"Match: {'✓' if message == decrypted else '✗'}")
    
    print(f"\n\n2. BRUTE FORCE DEMONSTRATION")
    print("-" * 40)
    
    # Brute force example
    secret_message = "Meet me at midnight"
    secret_shift = 13
    encrypted_secret = caesar_encrypt(secret_message, secret_shift)
    
    print(f"Intercepted message: {encrypted_secret}")
    print("Attempting brute force decryption...")
    
    results = brute_force_decrypt(encrypted_secret)
    for shift, decrypted in results.items():
        marker = " ← LIKELY MATCH" if shift == secret_shift else ""
        print(f"Shift {shift:2d}: {decrypted}{marker}")

if __name__ == "__main__":
    run_demo()
