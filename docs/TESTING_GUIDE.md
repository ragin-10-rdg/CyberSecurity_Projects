# Testing Guide for Cybersecurity Tools Suite

This guide provides comprehensive instructions for testing all tools with the provided mock data and test cases.

## 🚀 Quick Start Testing

### Run All Demos at Once
```bash
python run_all_demos.py
```
This master script will run automated demos for Caesar Cipher, Image Encryption, and Password Checker tools.

## 🔧 Individual Tool Testing

### 1. Caesar Cipher Tool
**Location**: `CaesarCipher/`

**Test Data**: `test_data.txt` - Contains various test messages with expected outputs

**Automated Demo**:
```bash
cd CaesarCipher
python demo_caesar.py
```

**Manual Testing**:
```bash
python caesar_cipher.py
```
- Try encrypting "Hello World!" with shift 3 (should get "Khoor Zruog!")
- Test brute force with "Wklv lv d whvw phvvdjh" (encrypted with shift 3)

### 2. Image Encryption Tool
**Location**: `ImageEncryption/`

**Generate Test Images**:
```bash
cd ImageEncryption
python create_sample_image.py
```

**Automated Demo**:
```bash
python demo_image_encryption.py
```

**Manual Testing**:
```bash
python image_encryption.py
```
- Use generated images in `sample_images/` folder
- Test XOR encryption with key seed 42
- Test pixel shift with shift value 75

### 3. Password Checker Tool
**Location**: `PasswordChecker/`

**Test Data**: `test_passwords.txt` - Contains weak, medium, and strong password examples

**Automated Demo**:
```bash
cd PasswordChecker
python demo_password_checker.py
```

**Manual Testing**:
```bash
python password_checker.py
```
- Test weak password: "password123"
- Test medium password: "MyPass123!"
- Test strong password: "Tr@v3l!ng*Ar0und&W0rld"

### 4. Keylogger Tool ⚠️
**Location**: `Keylogger/`

**Sample Data**: `sample_keylog.txt` - Example of captured keystrokes

**Manual Testing Only** (requires user interaction):
```bash
cd Keylogger
python keylogger.py
```
- ⚠️ **ETHICAL USE ONLY** - requires consent
- Start logging and type some test text
- Stop with Ctrl+C and view the generated keylog.txt

### 5. Packet Sniffer Tool ⚠️
**Location**: `PacketSniffer/`

**Sample Data**: `sample_network_data.txt` - Example network traffic captures

**Manual Testing Only** (requires admin privileges):
```bash
# Windows (Run as Administrator)
cd PacketSniffer
python packet_sniffer.py

# Linux/macOS (Run with sudo)
cd PacketSniffer
sudo python3 packet_sniffer.py
```
- ⚠️ **REQUIRES ADMIN PRIVILEGES** and **ETHICAL USE ONLY**
- Configure settings before starting capture
- Test with limited packet capture (e.g., 10 packets)

## 📊 Expected Test Results

### Caesar Cipher
- "Hello World!" + shift 3 → "Khoor Zruog!"
- Brute force should show all 26 possible decryptions
- Case preservation and special characters unchanged

### Image Encryption
- Original images should be visually scrambled when encrypted
- Decryption should restore original image exactly
- Different encryption methods produce different visual effects

### Password Checker
- "password123" → Weak (multiple issues)
- "MyPass123!" → Medium (good variety, contains dictionary word)
- "Tr@v3l!ng*Ar0und&W0rld" → Strong (excellent in all categories)

### Keylogger
- Should capture all keystrokes with timestamps
- Special keys logged as readable names (SPACE, ENTER, etc.)
- Session markers show start/end times

### Packet Sniffer
- Should display IP addresses, protocols, and ports
- Payload shown in both printable and hex format
- Protocol filtering should work correctly

## 🛠️ Troubleshooting

### Common Issues

**Import Errors**:
```bash
pip install Pillow numpy pynput scapy
```

**Permission Denied (Packet Sniffer)**:
- Run as Administrator (Windows) or with sudo (Linux/macOS)

**No Network Packets Captured**:
- Ensure network activity is occurring
- Try different network interface
- Check firewall settings

**Keylogger Not Working**:
- May be blocked by antivirus software
- Add exception for educational use
- Ensure proper permissions

### Dependency Installation
```bash
# For Image Encryption
pip install Pillow numpy

# For Keylogger  
pip install pynput

# For Packet Sniffer
pip install scapy
```

## 📁 Test Data Summary

| Tool | Test Files | Purpose |
|------|------------|---------|
| Caesar Cipher | `test_data.txt`, `demo_caesar.py` | Sample messages and automated testing |
| Image Encryption | `create_sample_image.py`, `demo_image_encryption.py` | Generate test images and run demos |
| Password Checker | `test_passwords.txt`, `demo_password_checker.py` | Password examples and strength analysis |
| Keylogger | `sample_keylog.txt` | Example keystroke capture output |
| Packet Sniffer | `sample_network_data.txt` | Example network traffic data |

## ⚖️ Ethical Testing Reminders

- **Only test on systems you own** or have explicit permission to use
- **Keylogger and Packet Sniffer** require special ethical considerations
- **Always accept ethical disclaimers** when prompted
- **Use for educational purposes only**
- **Follow all applicable laws and regulations**

## 🎯 Learning Objectives

After testing these tools, you should understand:
- Classical vs. modern encryption techniques
- Password security best practices
- Network protocol structures
- Endpoint security monitoring
- Ethical considerations in cybersecurity tools

---

**Remember: Use all tools responsibly and ethically!**
