#!/usr/bin/env python3
"""
Dashboard Launcher - Creates and opens a local HTML dashboard
"""

import os
import sys
import webbrowser
import subprocess
from datetime import datetime

def create_html_dashboard():
    """Create a standalone HTML dashboard."""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cybersecurity Tools Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #f5f5f5;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: rgba(22, 33, 62, 0.8);
            border-radius: 15px;
            border: 1px solid #0f3460;
        }
        
        .header h1 {
            font-size: 2.5rem;
            color: #e94560;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .warning {
            background: rgba(255, 193, 7, 0.2);
            border: 1px solid #ffc107;
            border-radius: 10px;
            padding: 15px;
            margin: 20px 0;
            text-align: center;
        }
        
        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }
        
        .tool-card {
            background: rgba(22, 33, 62, 0.8);
            border: 1px solid #0f3460;
            border-radius: 15px;
            padding: 25px;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .tool-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(233, 69, 96, 0.3);
            border-color: #e94560;
        }
        
        .tool-icon {
            font-size: 3rem;
            text-align: center;
            margin-bottom: 15px;
        }
        
        .tool-title {
            font-size: 1.5rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
            color: #e94560;
        }
        
        .tool-description {
            text-align: center;
            opacity: 0.9;
            margin-bottom: 15px;
        }
        
        .tool-features {
            list-style: none;
            margin-bottom: 20px;
        }
        
        .tool-features li {
            padding: 5px 0;
            padding-left: 20px;
            position: relative;
        }
        
        .tool-features li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #28a745;
            font-weight: bold;
        }
        
        .launch-btn {
            background: linear-gradient(45deg, #0f3460, #e94560);
            border: none;
            border-radius: 25px;
            padding: 12px 25px;
            color: white;
            font-weight: 500;
            cursor: pointer;
            width: 100%;
            transition: all 0.3s ease;
        }
        
        .launch-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(233, 69, 96, 0.4);
        }
        
        .badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.8rem;
            margin: 2px;
        }
        
        .badge-warning {
            background: #ffc107;
            color: #000;
        }
        
        .badge-danger {
            background: #dc3545;
            color: #fff;
        }
        
        .badge-primary {
            background: #0f3460;
            color: #fff;
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛡️ Cybersecurity Tools Dashboard</h1>
            <p>A comprehensive collection of educational cybersecurity tools</p>
            <div class="warning">
                <strong>⚠️ Educational Use Only:</strong> These tools are designed for learning and authorized security testing. Always use ethically and legally.
            </div>
        </div>
        
        <div class="tools-grid">
            <div class="tool-card" onclick="launchTool('caesar')">
                <div class="tool-icon">🔐</div>
                <div class="tool-title">Caesar Cipher</div>
                <div class="tool-description">Classical encryption/decryption tool with brute force analysis</div>
                <ul class="tool-features">
                    <li>Encrypt text with custom shift</li>
                    <li>Decrypt with known shift</li>
                    <li>Brute force analysis</li>
                </ul>
                <span class="badge badge-primary">Cryptography</span>
                <button class="launch-btn">Launch Tool</button>
            </div>
            
            <div class="tool-card" onclick="launchTool('password')">
                <div class="tool-icon">🔑</div>
                <div class="tool-title">Password Checker</div>
                <div class="tool-description">Analyze password strength and security</div>
                <ul class="tool-features">
                    <li>Comprehensive strength analysis</li>
                    <li>Entropy calculation</li>
                    <li>Security recommendations</li>
                </ul>
                <span class="badge badge-primary">Security Analysis</span>
                <button class="launch-btn">Launch Tool</button>
            </div>
            
            <div class="tool-card" onclick="launchTool('image')">
                <div class="tool-icon">🖼️</div>
                <div class="tool-title">Image Encryption</div>
                <div class="tool-description">Encrypt/decrypt images using pixel manipulation</div>
                <ul class="tool-features">
                    <li>XOR encryption method</li>
                    <li>Pixel shifting algorithm</li>
                    <li>Format preservation</li>
                </ul>
                <span class="badge badge-primary">Cryptography</span>
                <button class="launch-btn">Launch Tool</button>
            </div>
            
            <div class="tool-card" onclick="launchTool('keylogger')">
                <div class="tool-icon">⌨️</div>
                <div class="tool-title">Keylogger</div>
                <div class="tool-description">Educational keystroke monitoring tool</div>
                <ul class="tool-features">
                    <li>Real-time keystroke logging</li>
                    <li>Session management</li>
                    <li>Ethical safeguards</li>
                </ul>
                <span class="badge badge-primary">Monitoring</span>
                <span class="badge badge-warning">⚠️ Consent Required</span>
                <button class="launch-btn">Launch Tool</button>
            </div>
            
            <div class="tool-card" onclick="launchTool('packet')">
                <div class="tool-icon">🌐</div>
                <div class="tool-title">Packet Sniffer</div>
                <div class="tool-description">Network traffic analysis and monitoring</div>
                <ul class="tool-features">
                    <li>Protocol parsing</li>
                    <li>Payload inspection</li>
                    <li>Traffic filtering</li>
                </ul>
                <span class="badge badge-primary">Network Security</span>
                <span class="badge badge-danger">🛡️ Admin Required</span>
                <button class="launch-btn">Launch Tool</button>
            </div>
            
            <div class="tool-card" onclick="launchTool('demo')">
                <div class="tool-icon">🚀</div>
                <div class="tool-title">Run All Demos</div>
                <div class="tool-description">Execute demonstrations of all available tools</div>
                <ul class="tool-features">
                    <li>Automated testing</li>
                    <li>Sample data included</li>
                    <li>Comprehensive overview</li>
                </ul>
                <span class="badge badge-primary">Demo Suite</span>
                <button class="launch-btn">Launch Demos</button>
            </div>
        </div>
        
        <div class="footer">
            <p>Created for cybersecurity education and awareness. Always prioritize ethical behavior and legal compliance.</p>
            <p>Current Time: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
        </div>
    </div>
    
    <script>
        function launchTool(toolType) {
            const batchFiles = {
                'caesar': 'launch_caesar.bat',
                'password': 'launch_password.bat',
                'image': 'launch_image.bat',
                'keylogger': 'launch_keylogger.bat',
                'packet': 'launch_packet.bat',
                'demo': 'launch_demo.bat'
            };
            
            const commands = {
                'caesar': 'python CaesarCipher/caesar_cipher.py',
                'password': 'python PasswordChecker/password_checker.py',
                'image': 'python ImageEncryption/image_encryption.py',
                'keylogger': 'python Keylogger/keylogger.py',
                'packet': 'python PacketSniffer/packet_sniffer.py',
                'demo': 'python run_all_demos.py'
            };
            
            const toolNames = {
                'caesar': 'Caesar Cipher',
                'password': 'Password Checker',
                'image': 'Image Encryption',
                'keylogger': 'Keylogger',
                'packet': 'Packet Sniffer',
                'demo': 'Demo Suite'
            };
            
            if (toolType === 'keylogger' || toolType === 'packet') {
                const consent = confirm(
                    `⚠️ ETHICAL WARNING for ${toolNames[toolType]}:\\n\\n` +
                    `This tool is for educational purposes only.\\n` +
                    `Only use on systems you own or have explicit permission to monitor.\\n` +
                    `Unauthorized use is illegal and unethical.\\n\\n` +
                    `Do you understand and agree to use this tool ethically?`
                );
                
                if (!consent) {
                    alert('❌ Ethical consent required to proceed.');
                    return;
                }
            }
            
            // Try to launch batch file or provide instructions
            const batchFile = batchFiles[toolType];
            const commandText = commands[toolType];
            
            const instructions = 
                `🚀 To launch ${toolNames[toolType]}:\\n\\n` +
                `Option 1: Double-click the file "${batchFile}" in your project folder\\n\\n` +
                `Option 2: Run this command in terminal:\\n${commandText}\\n\\n` +
                `Click OK to copy the command to clipboard.`;
            
            const result = confirm(instructions);
            
            if (result) {
                // Copy command to clipboard
                navigator.clipboard.writeText(commandText).then(() => {
                    alert(`✅ Command copied to clipboard!\\n\\nYou can now:\\n1. Paste in terminal, OR\\n2. Double-click "${batchFile}" in your project folder`);
                }).catch(() => {
                    // Fallback if clipboard API fails
                    prompt('Copy this command and run it in your terminal:', commandText);
                });
            }
        }
        
        // Add some interactive effects
        document.addEventListener('DOMContentLoaded', function() {
            const cards = document.querySelectorAll('.tool-card');
            cards.forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-5px) scale(1.02)';
                });
                
                card.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0) scale(1)';
                });
            });
        });
    </script>
</body>
</html>"""
    
    return html_content

def launch_tool_command(tool_type):
    """Launch a specific tool via command line."""
    commands = {
        'caesar': ['python', 'CaesarCipher/caesar_cipher.py'],
        'password': ['python', 'PasswordChecker/password_checker.py'],
        'image': ['python', 'ImageEncryption/image_encryption.py'],
        'keylogger': ['python', 'Keylogger/keylogger.py'],
        'packet': ['python', 'PacketSniffer/packet_sniffer.py'],
        'demo': ['python', 'run_all_demos.py']
    }
    
    if tool_type in commands:
        try:
            subprocess.Popen(commands[tool_type], creationflags=subprocess.CREATE_NEW_CONSOLE)
            return True
        except Exception as e:
            print(f"Error launching {tool_type}: {e}")
            return False
    return False

def launch_command_line_dashboard():
    """Launch a simple command line dashboard."""
    print("\n💻 COMMAND LINE DASHBOARD")
    print("=" * 50)
    
    tools = {
        '1': {'name': 'Caesar Cipher', 'cmd': 'caesar', 'icon': '🔐'},
        '2': {'name': 'Password Checker', 'cmd': 'password', 'icon': '🔑'},
        '3': {'name': 'Image Encryption', 'cmd': 'image', 'icon': '🖼️'},
        '4': {'name': 'Keylogger', 'cmd': 'keylogger', 'icon': '⌨️'},
        '5': {'name': 'Packet Sniffer', 'cmd': 'packet', 'icon': '🌐'},
        '6': {'name': 'Run All Demos', 'cmd': 'demo', 'icon': '🚀'}
    }
    
    while True:
        print("\n📋 Available Tools:")
        print("-" * 30)
        for key, tool in tools.items():
            print(f"{key}. {tool['icon']} {tool['name']}")
        print("0. 🚪 Exit")
        
        choice = input("\nSelect tool (0-6): ").strip()
        
        if choice == '0':
            print("👋 Goodbye!")
            break
        elif choice in tools:
            tool = tools[choice]
            print(f"🚀 Launching {tool['name']}...")
            
            # Special handling for sensitive tools
            if choice in ['4', '5']:  # Keylogger or Packet Sniffer
                consent = input(f"⚠️ {tool['name']} requires ethical consent. Proceed? (y/n): ").lower()
                if consent != 'y':
                    print("❌ Operation cancelled")
                    continue
            
            if launch_tool_command(tool['cmd']):
                print(f"✅ {tool['name']} launched in new window")
            else:
                print(f"❌ Failed to launch {tool['name']}")
        else:
            print("❌ Invalid choice")

def create_batch_files():
    """Create batch files for launching tools from HTML dashboard."""
    batch_commands = {
        'launch_caesar.bat': 'python CaesarCipher/caesar_cipher.py\npause',
        'launch_password.bat': 'python PasswordChecker/password_checker.py\npause',
        'launch_image.bat': 'python ImageEncryption/image_encryption.py\npause',
        'launch_keylogger.bat': 'python Keylogger/keylogger.py\npause',
        'launch_packet.bat': 'python PacketSniffer/packet_sniffer.py\npause',
        'launch_demo.bat': 'python run_all_demos.py\npause'
    }
    
    created_files = []
    for filename, content in batch_commands.items():
        try:
            with open(filename, 'w') as f:
                f.write(content)
            created_files.append(filename)
        except Exception as e:
            print(f"⚠️ Could not create {filename}: {e}")
    
    return created_files

def main():
    """Main launcher function."""
    print("🛡️ Cybersecurity Tools Dashboard Launcher")
    print("=" * 50)
    
    # Create batch files for tool launching
    batch_files = create_batch_files()
    if batch_files:
        print(f"✅ Created {len(batch_files)} launcher batch files")
    
    # Create HTML dashboard with fallback locations
    html_content = create_html_dashboard()
    html_files = ['cybersecurity_dashboard.html', 'dashboard.html', 'temp_dashboard.html']
    html_file = None
    
    for filename in html_files:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            html_file = filename
            print(f"✅ HTML dashboard created: {html_file}")
            break
        except PermissionError:
            print(f"⚠️ Permission denied for {filename}, trying alternative...")
            continue
        except Exception as e:
            print(f"⚠️ Error with {filename}: {e}, trying alternative...")
            continue
    
    if not html_file:
        print("❌ Could not create HTML file due to permissions.")
        print("🔧 Alternative: Use command line dashboard instead")
        print("\nOptions:")
        print("1. Run as administrator")
        print("2. Use command line interface")
        choice = input("Select option (1-2): ").strip()
        
        if choice == '1':
            print("Please restart this program as administrator")
            return
        elif choice == '2':
            print("💻 Launching command line dashboard...")
            launch_command_line_dashboard()
            return
        else:
            print("❌ Invalid choice")
            return
    
    # Open in browser
    try:
        file_path = os.path.abspath(html_file)
        webbrowser.open(f'file://{file_path}')
        print(f"🌐 Opening dashboard in browser...")
        print(f"📁 File location: {file_path}")
    except Exception as e:
        print(f"❌ Error opening browser: {e}")
        print(f"📁 Manually open: {os.path.abspath(html_file)}")
    
    print("\n📋 Available Options:")
    print("1. 🌐 HTML Dashboard (opened in browser)")
    print("2. 💻 Command Line Dashboard")
    print("3. 🚀 Run All Demos")
    print("0. 🚪 Exit")
    
    while True:
        choice = input("\nSelect option (0-3): ").strip()
        
        if choice == '0':
            print("👋 Goodbye!")
            break
        elif choice == '1':
            print("🌐 HTML dashboard should be open in your browser.")
            print(f"📁 If not, open: {os.path.abspath(html_file)}")
        elif choice == '2':
            print("💻 Launching command line dashboard...")
            launch_tool_command('simple')
        elif choice == '3':
            print("🚀 Running all demos...")
            launch_tool_command('demo')
        else:
            print("❌ Invalid choice. Please select 0-3.")

if __name__ == "__main__":
    main()
