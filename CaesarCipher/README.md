# Caesar Cipher Tool

A simple implementation of the Caesar cipher encryption/decryption algorithm for educational purposes.

## Purpose

The Caesar cipher is one of the simplest and most widely known encryption techniques. It shifts each letter in the plaintext by a fixed number of positions down the alphabet. This tool demonstrates basic cryptographic concepts and is useful for learning about classical ciphers.

## Features

- **Encrypt text** using Caesar cipher with custom shift value
- **Decrypt text** when you know the shift value
- **Brute force decrypt** to try all possible shift values
- Preserves case (uppercase/lowercase)
- Leaves non-alphabetic characters unchanged

## How to Run

1. Navigate to the CaesarCipher directory
2. Run the script:
   ```bash
   python caesar_cipher.py
   ```

## Dependencies

No external libraries required - uses only Python standard library.

## Example Usage

### Encryption
```
Input: "Hello World!"
Shift: 3
Output: "Khoor Zruog!"
```

### Decryption
```
Input: "Khoor Zruog!"
Shift: 3
Output: "Hello World!"
```

### Brute Force
```
Input: "Khoor Zruog!"
Output: Shows all 26 possible decryptions with different shift values
```

## Educational Note

This tool is designed for educational purposes to understand basic encryption concepts. The Caesar cipher is not secure for real-world applications and can be easily broken with frequency analysis or brute force attacks.
