#!/usr/bin/env python3
"""
Master Demo Script for Cybersecurity Tools Suite
Run demonstrations of all tools with test data.
"""

import os
import sys
import subprocess
import time

def run_demo_script(tool_dir, script_name, description):
    """Run a demo script and handle errors."""
    print(f"\n{'='*60}")
    print(f"RUNNING: {description}")
    print(f"{'='*60}")
    
    script_path = os.path.join(tool_dir, script_name)
    
    if not os.path.exists(script_path):
        print(f"❌ Demo script not found: {script_path}")
        return False
    
    try:
        # Change to the tool directory
        original_dir = os.getcwd()
        os.chdir(tool_dir)
        
        # Run the demo script
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Demo completed successfully!")
            print("\nOutput:")
            print(result.stdout)
        else:
            print("❌ Demo failed!")
            print("Error:", result.stderr)
        
        # Return to original directory
        os.chdir(original_dir)
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("⏰ Demo timed out (30 seconds)")
        os.chdir(original_dir)
        return False
    except Exception as e:
        print(f"❌ Error running demo: {e}")
        os.chdir(original_dir)
        return False

def check_dependencies():
    """Check if required dependencies are installed."""
    print("Checking dependencies...")
    
    dependencies = {
        'PIL': 'Pillow (for Image Encryption)',
        'numpy': 'numpy (for Image Encryption)',
        'pynput': 'pynput (for Keylogger)',
        'scapy': 'scapy (for Packet Sniffer)'
    }
    
    missing = []
    for module, description in dependencies.items():
        try:
            __import__(module)
            print(f"✅ {description}")
        except ImportError:
            print(f"❌ {description} - NOT INSTALLED")
            missing.append(module)
    
    if missing:
        print(f"\nTo install missing dependencies:")
        for module in missing:
            if module == 'PIL':
                print("pip install Pillow")
            else:
                print(f"pip install {module}")
        print()
    
    return len(missing) == 0

def main():
    """Run all tool demonstrations."""
    print("=" * 80)
    print("         CYBERSECURITY TOOLS SUITE - MASTER DEMO")
    print("=" * 80)
    print("This script will demonstrate all 5 cybersecurity tools with test data.")
    print("Each tool will be tested with sample inputs to show functionality.")
    print("=" * 80)
    
    # Check dependencies
    if not check_dependencies():
        print("\n⚠️  Some dependencies are missing. Install them for full functionality.")
        proceed = input("Continue anyway? (y/n): ").lower().strip()
        if proceed != 'y':
            return
    
    # Define demo configurations
    demos = [
        {
            'dir': 'CaesarCipher',
            'script': 'demo_caesar.py',
            'description': 'Caesar Cipher Encryption/Decryption Demo'
        },
        {
            'dir': 'ImageEncryption', 
            'script': 'demo_image_encryption.py',
            'description': 'Image Encryption Demo (requires Pillow & numpy)'
        },
        {
            'dir': 'PasswordChecker',
            'script': 'demo_password_checker.py', 
            'description': 'Password Strength Analysis Demo'
        }
    ]
    
    # Run demos
    results = {}
    for demo in demos:
        success = run_demo_script(demo['dir'], demo['script'], demo['description'])
        results[demo['description']] = success
        
        if success:
            time.sleep(2)  # Brief pause between demos
    
    # Show summary
    print(f"\n{'='*80}")
    print("DEMO SUMMARY")
    print(f"{'='*80}")
    
    for description, success in results.items():
        status = "✅ SUCCESS" if success else "❌ FAILED"
        print(f"{description:<50} {status}")
    
    # Show manual testing instructions
    print(f"\n{'='*80}")
    print("MANUAL TESTING INSTRUCTIONS")
    print(f"{'='*80}")
    
    print("\n🔐 KEYLOGGER TOOL:")
    print("- Requires manual testing due to interactive nature")
    print("- Run: python Keylogger/keylogger.py")
    print("- ⚠️  ETHICAL USE ONLY - requires user consent")
    
    print("\n🌐 PACKET SNIFFER TOOL:")
    print("- Requires administrator privileges")
    print("- Run: python PacketSniffer/packet_sniffer.py (as admin)")
    print("- ⚠️  ETHICAL USE ONLY - authorized networks only")
    
    print("\n📁 TEST DATA LOCATIONS:")
    print("- CaesarCipher/test_data.txt - Sample messages")
    print("- ImageEncryption/sample_images/ - Generated test images")
    print("- PasswordChecker/test_passwords.txt - Password examples")
    print("- Keylogger/sample_keylog.txt - Example keylog output")
    print("- PacketSniffer/sample_network_data.txt - Network traffic examples")
    
    print(f"\n{'='*80}")
    print("All available demos completed!")
    print("Check individual tool directories for more test data and examples.")
    print("Remember: Use all tools ethically and legally!")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
