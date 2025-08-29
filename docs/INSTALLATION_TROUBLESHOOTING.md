# Installation Troubleshooting Guide

## Common pip Installation Issues

### Issue: "Getting requirements to build wheel ... error"

This error typically occurs due to:
1. Outdated pip version
2. Missing build tools
3. Python version compatibility
4. Network/proxy issues

## Solutions

### Method 1: Update pip and setuptools
```bash
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel
```

### Method 2: Install packages individually
```bash
pip install Pillow
pip install numpy
pip install pynput
pip install scapy
```

### Method 3: Use conda (if available)
```bash
conda install pillow numpy
pip install pynput scapy
```

### Method 4: Install with --no-cache-dir
```bash
pip install --no-cache-dir -r requirements.txt
```

### Method 5: Install with --user flag
```bash
pip install --user -r requirements.txt
```

## Windows-Specific Solutions

### Install Microsoft C++ Build Tools
1. Download Visual Studio Build Tools from Microsoft
2. Install "C++ build tools" workload
3. Restart command prompt and try again

### Use pre-compiled wheels
```bash
pip install --only-binary=all -r requirements.txt
```

## Alternative: Minimal Installation

If you continue having issues, you can run most tools without all dependencies:

### Tools that work without external dependencies:
- **Caesar Cipher** (no dependencies needed)
- **Password Checker** (no dependencies needed)

### Tools requiring specific packages:
- **Image Encryption**: `pip install Pillow numpy`
- **Keylogger**: `pip install pynput`
- **Packet Sniffer**: `pip install scapy`

## Testing Installation

After installation, test each package:

```python
# Test Pillow
try:
    from PIL import Image
    print("✅ Pillow installed successfully")
except ImportError:
    print("❌ Pillow not installed")

# Test numpy
try:
    import numpy
    print("✅ numpy installed successfully")
except ImportError:
    print("❌ numpy not installed")

# Test pynput
try:
    from pynput import keyboard
    print("✅ pynput installed successfully")
except ImportError:
    print("❌ pynput not installed")

# Test scapy
try:
    import scapy
    print("✅ scapy installed successfully")
except ImportError:
    print("❌ scapy not installed")
```

## If All Else Fails

You can still use the cybersecurity tools! The Caesar Cipher and Password Checker tools work with just Python standard library:

```bash
cd CaesarCipher
python caesar_cipher.py

cd ../PasswordChecker  
python password_checker.py
```

These tools provide excellent learning opportunities even without the image encryption, keylogger, and packet sniffer components.
