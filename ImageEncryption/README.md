# Image Encryption Tool

A Python tool for encrypting and decrypting images using pixel manipulation techniques.

## Purpose

This tool demonstrates basic image encryption concepts using two different methods:
1. **XOR Encryption**: Uses bitwise XOR operations with a generated key
2. **Pixel Shift**: Simple encryption by shifting pixel values

## Features

- **XOR-based encryption/decryption** with customizable key seeds
- **Pixel shift encryption/decryption** with adjustable shift values
- Preserves image format and dimensions
- Supports common image formats (JPEG, PNG, BMP, etc.)
- Reversible encryption (decrypt restores original image)

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Navigate to the ImageEncryption directory

3. Run the script:
   ```bash
   python image_encryption.py
   ```

## Dependencies

- **Pillow**: For image processing
- **numpy**: For array operations

## Example Usage

### XOR Encryption
```
Input: sample.jpg
Key Seed: 123
Output: encrypted_sample.jpg (visually scrambled)

Decryption with same key seed (123) restores original image
```

### Pixel Shift Encryption
```
Input: photo.png
Shift Value: 75
Output: encrypted_photo.png (color-shifted image)

Decryption with same shift value (75) restores original colors
```

## Sample Workflow

1. Place an image file in the same directory
2. Run the tool and choose option 1 (XOR encryption)
3. Enter the image path and desired output path
4. Enter a key seed (remember this number!)
5. The encrypted image will be saved
6. To decrypt, use option 2 with the same key seed

## Security Note

This tool is for educational purposes only. The encryption methods used here are not cryptographically secure and should not be used for protecting sensitive data. Real-world image encryption requires more sophisticated algorithms and proper key management.
