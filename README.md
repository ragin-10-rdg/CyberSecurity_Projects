# 🛡️ Cybersecurity Tools Suite

A comprehensive collection of educational cybersecurity tools with an integrated web dashboard for easy access and management.

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](README.md)

## 📋 Table of Contents
- [📖 Overview](#-overview)
- [⚡ Quick Installation](#-quick-installation)
- [🔧 System Requirements](#-system-requirements)
- [📥 Installation Methods](#-installation-methods)
- [🚀 Getting Started](#-getting-started)
- [🔧 Tools Overview](#-tools-overview)
- [📁 Project Structure](#-project-structure)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [⚖️ Legal & Ethical Guidelines](#️-legal--ethical-guidelines)

## 📖 Overview

This educational cybersecurity suite contains **5 powerful security tools** with a unified dashboard interface. Perfect for students, educators, and security professionals learning cybersecurity concepts.

**🎯 What You Get:**
- 🔐 **Caesar Cipher Tool** - Classical encryption/decryption
- 🖼️ **Image Encryption Tool** - Pixel manipulation encryption
- 🔑 **Password Checker Tool** - Comprehensive strength analysis
- ⌨️ **Keylogger Tool** - Educational keystroke monitoring
- 🌐 **Packet Sniffer Tool** - Network traffic analysis
- 🚀 **Unified Dashboard** - Web interface for all tools

## ⚡ Quick Installation

### Option 1: Clone Repository (Recommended)
```bash
# Clone the repository
git clone https://github.com/ragin-10-rdg/CyberSecurity_Projects.git

# Navigate to project directory
cd CyberSecurity_Projects/Cybersecurity-Tools-Suite_Projects

# Install dependencies
pip install -r requirements.txt

# Launch dashboard
python dashboard_launcher.py
```

### Option 2: Download ZIP
1. **Download**: Click [here](https://github.com/ragin-10-rdg/CyberSecurity_Projects/archive/refs/heads/main.zip) to download ZIP
2. **Extract**: Unzip to your desired location
3. **Navigate**: Open terminal in `Cybersecurity-Tools-Suite_Projects` folder
4. **Install**: Run `pip install -r requirements.txt`
5. **Launch**: Run `python dashboard_launcher.py`

## 🔧 System Requirements

### Minimum Requirements
| Component | Requirement |
|-----------|-------------|
| **Python** | 3.6 or higher |
| **RAM** | 512 MB available |
| **Storage** | 100 MB free space |
| **OS** | Windows 7+, macOS 10.12+, Linux (any modern distro) |

### Additional Requirements
- **Administrator privileges** (for Keylogger and Packet Sniffer)
- **Internet connection** (for initial dependency installation)
- **Modern web browser** (for dashboard interface)

### Check Your Python Version
```bash
python --version
# Should show Python 3.6 or higher
```

## 📥 Installation Methods

### Method 1: Automatic Installation (Windows)
```batch
# Download and run this one-liner in Command Prompt
curl -o install.bat https://raw.githubusercontent.com/ragin-10-rdg/CyberSecurity_Projects/main/install.bat && install.bat
```

### Method 2: Manual Installation (All Platforms)

#### Step 1: Download Project
```bash
# Using Git
git clone https://github.com/ragin-10-rdg/CyberSecurity_Projects.git
cd CyberSecurity_Projects/Cybersecurity-Tools-Suite_Projects

# OR download ZIP and extract
```

#### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv cybersecurity_env

# Activate virtual environment
# Windows:
cybersecurity_env\Scripts\activate
# macOS/Linux:
source cybersecurity_env/bin/activate
```

#### Step 3: Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

#### Step 4: Test Installation
```bash
# Run quick test
python run_all_demos.py

# Launch dashboard
python dashboard_launcher.py
```

### Method 3: Docker Installation (Advanced)
```bash
# Build Docker image
docker build -t cybersecurity-suite .

# Run container
docker run -p 5000:5000 cybersecurity-suite
```

## 🚀 Getting Started

### 🎯 Launch Dashboard (Recommended)
```bash
python dashboard_launcher.py
```

**What happens next:**
1. 🌐 **Web dashboard** opens in your browser
2. 📁 **Batch files** are generated for quick access
3. 💻 **Command line interface** available as backup
4. 🎮 **Interactive menu** guides you through tools

### 🔧 Run Individual Tools
```bash
# Caesar Cipher
python CaesarCipher/caesar_cipher.py

# Password Checker
python PasswordChecker/password_checker.py

# Image Encryption
python ImageEncryption/image_encryption.py

# Keylogger (requires admin)
python Keylogger/keylogger.py

# Packet Sniffer (requires admin)
python PacketSniffer/packet_sniffer.py
```

### 🎬 Run All Demonstrations
```bash
python run_all_demos.py
```

## 🔧 Tools Overview

| Tool | Purpose | Dependencies | Admin Required |
|------|---------|--------------|----------------|
| 🔐 **Caesar Cipher** | Classical encryption learning | None | ❌ |
| 🔑 **Password Checker** | Password strength analysis | None | ❌ |
| 🖼️ **Image Encryption** | Image-based encryption | Pillow, numpy | ❌ |
| ⌨️ **Keylogger** | Keystroke monitoring education | pynput | ✅ |
| 🌐 **Packet Sniffer** | Network traffic analysis | scapy (optional) | ✅ |

### Detailed Tool Features

#### 🔐 Caesar Cipher Tool
```bash
python CaesarCipher/caesar_cipher.py
```
- ✅ Encrypt/decrypt text with custom shifts
- ✅ Brute force analysis (all possible shifts)
- ✅ Interactive CLI with examples
- ✅ Educational explanations

#### 🔑 Password Checker Tool
```bash
python PasswordChecker/password_checker.py
```
- ✅ Comprehensive strength analysis
- ✅ Entropy calculation
- ✅ Security recommendations
- ✅ Common password detection

#### 🖼️ Image Encryption Tool
```bash
python ImageEncryption/image_encryption.py
```
- ✅ XOR encryption methods
- ✅ Pixel shifting techniques
- ✅ Multiple image format support
- ✅ Before/after comparison

#### ⌨️ Keylogger Tool ⚠️
```bash
# Requires administrator privileges
python Keylogger/keylogger.py
```
- ✅ Real-time keystroke logging
- ✅ Session management
- ✅ Built-in ethical safeguards
- ✅ Consent mechanisms

#### 🌐 Packet Sniffer Tool ⚠️
```bash
# Requires administrator privileges
python PacketSniffer/packet_sniffer.py
```
- ✅ Network protocol analysis
- ✅ Payload inspection
- ✅ Traffic filtering
- ✅ Export capabilities

## 📁 Project Structure

```
Cybersecurity-Tools-Suite_Projects/
│
├── 🚀 dashboard_launcher.py         # MAIN ENTRY POINT
├── 🎬 run_all_demos.py             # Run all demonstrations
├── 📄 requirements.txt             # Python dependencies
├── 📖 README.md                    # This file
├── 🔧 INSTALLATION_TROUBLESHOOTING.md
├── 🧪 TESTING_GUIDE.md
│
├── CaesarCipher/                   # Classical encryption tool
│   ├── caesar_cipher.py            # Main tool
│   ├── demo_caesar.py              # Demonstration
│   ├── requirements.txt            # Tool-specific deps
│   └── README.md                   # Tool documentation
│
├── ImageEncryption/                # Image encryption tool
│   ├── image_encryption.py         # Main tool
│   ├── demo_image_encryption.py    # Demonstration
│   ├── create_sample_image.py      # Sample image generator
│   └── README.md
│
├── PasswordChecker/                # Password analysis tool
│   ├── password_checker.py         # Main tool
│   ├── demo_password_checker.py    # Demonstration
│   └── README.md
│
├── Keylogger/                      # Educational keylogger
│   ├── keylogger.py                # Main tool
│   ├── sample_keylog.txt           # Example output
│   └── README.md
│
├── PacketSniffer/                  # Network analysis tool
│   ├── packet_sniffer.py           # Main tool
│   ├── sample_network_data.txt     # Example output
│   └── README.md
│
└── Generated Files/                # Auto-generated by dashboard
    ├── launch_caesar.bat           # Quick launch files
    ├── launch_password.bat
    ├── launch_image.bat
    ├── launch_keylogger.bat
    ├── launch_packet.bat
    ├── launch_demo.bat
    └── cybersecurity_dashboard.html # Web dashboard
```

## 🛠️ Troubleshooting

### Common Installation Issues

#### ❌ "Python not found"
```bash
# Install Python from python.org
# Add Python to PATH during installation
# Verify installation:
python --version
```

#### ❌ "pip not found"
```bash
# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

#### ❌ "Permission denied" (Windows)
```batch
# Run Command Prompt as Administrator
# Right-click Command Prompt → "Run as administrator"
```

#### ❌ "Permission denied" (macOS/Linux)
```bash
# Use sudo for system-wide installation
sudo pip install -r requirements.txt

# OR use user installation
pip install --user -r requirements.txt
```

#### ❌ "Module not found" errors
```bash
# Reinstall dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# Check virtual environment activation
which python
```

### Tool-Specific Issues

#### Keylogger Issues
```bash
# Windows: Run as Administrator
# macOS: Grant accessibility permissions
# Linux: Check user permissions
```

#### Packet Sniffer Issues
```bash
# Install additional dependencies
pip install scapy
# Run with administrator privileges
```

#### Image Encryption Issues
```bash
# Install image processing libraries
pip install Pillow numpy
```

### Getting Help
- 📖 Check `INSTALLATION_TROUBLESHOOTING.md`
- 🧪 Run `TESTING_GUIDE.md` procedures
- 🐛 Report issues on GitHub
- 📧 Contact maintainers

## ⚖️ Legal & Ethical Guidelines

### 🔴 IMPORTANT LEGAL NOTICE
These tools are provided for **educational purposes only**. Users must:

- ✅ Only use on systems they own or have explicit written permission to test
- ✅ Comply with all applicable local, state, and federal laws
- ✅ Respect privacy and confidentiality
- ✅ Use tools responsibly and ethically
- ❌ Never use for unauthorized access or malicious purposes
- ❌ Never deploy without proper consent and documentation

### 📚 Educational Use Cases
- **Learning**: Understanding cybersecurity concepts and techniques
- **Authorized Testing**: Penetration testing with proper documentation
- **Security Research**: Academic and professional research projects
- **Training**: Security awareness and vulnerability demonstrations

### 🚨 Legal Requirements
- **Written Permission**: Required for testing on systems you don't own
- **Documentation**: Keep records of authorized testing activities
- **Compliance**: Follow all local, state, federal, and international laws
- **Professional Ethics**: Adhere to cybersecurity professional standards

### 🛡️ Responsible Disclosure
If you discover vulnerabilities during authorized testing:
1. **Document findings** responsibly
2. **Report to appropriate parties** (system owners, vendors)
3. **Follow coordinated disclosure** timelines
4. **Respect confidentiality** agreements

## 📄 License & Disclaimer

### License
This project is provided under an educational license. See `LICENSE` file for details.

### Disclaimer
The authors and contributors:
- ❌ Are **not responsible** for any misuse of these tools
- ❌ Do **not encourage** illegal or unethical activities  
- ✅ Provide tools **solely for educational** and authorized purposes
- ✅ **Strongly recommend** understanding applicable laws before use

### Support & Community
- 🌟 **Star this repository** if you find it helpful
- 🐛 **Report issues** on GitHub Issues
- 🤝 **Contribute** following our contribution guidelines
- 📧 **Contact maintainers** for questions or collaboration

---

**⚠️ Remember: Use responsibly. Learn ethically. Stay legal.**

*Created for cybersecurity education and awareness. Always prioritize ethical behavior and legal compliance.*
