# Keylogger Tool

An educational keylogger for cybersecurity learning and authorized security testing.

## ⚠️ ETHICAL DISCLAIMER

**THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY**

- Only use on systems you **own** or have **explicit written permission** to monitor
- Unauthorized keylogging is **illegal** and **unethical**
- Never use this tool for malicious purposes
- Always respect privacy and follow applicable laws
- Intended for cybersecurity education and authorized penetration testing

## Purpose

This tool demonstrates how keyloggers work and helps understand:
- Keystroke capture techniques
- Security monitoring concepts
- The importance of endpoint protection
- Ethical considerations in cybersecurity

## Features

- **Real-time keystroke logging** with timestamps
- **Special key detection** (Enter, Space, Shift, etc.)
- **Buffered writing** for performance
- **Session management** with start/stop controls
- **Log viewing** and management
- **Ethical safeguards** and warnings

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Navigate to the Keylogger directory

3. Run the script:
   ```bash
   python keylogger.py
   ```

4. **Read and accept the ethical disclaimer**

5. Choose option 1 to start logging

6. Press Ctrl+C to stop logging

## Dependencies

- **pynput**: For keyboard event capture

## Usage Instructions

### Starting the Keylogger
1. Run the script and choose option 1
2. Read and accept the ethical disclaimer
3. Keylogger will start capturing keystrokes
4. All keystrokes are saved to `keylog.txt` with timestamps

### Stopping the Keylogger
- Press Ctrl+C while logging is active, or
- Choose option 2 from the menu

### Viewing Logs
- Choose option 3 to view recent log entries
- Specify number of lines to display

### Managing Logs
- Option 4: Clear all logs
- Option 5: Change log file location

## Log Format

```
[2024-08-29 13:06:15] Key: 'h'
[2024-08-29 13:06:15] Key: 'e'
[2024-08-29 13:06:16] Key: 'l'
[2024-08-29 13:06:16] Key: 'l'
[2024-08-29 13:06:16] Key: 'o'
[2024-08-29 13:06:17] Special Key: SPACE
[2024-08-29 13:06:18] Special Key: ENTER
```

## Security Considerations

### Detection
- Modern antivirus software may flag this as malware
- Windows Defender might block execution
- Add exception if needed for educational use

### Legal Compliance
- Ensure you have proper authorization
- Document your testing activities
- Follow organizational security policies
- Comply with local privacy laws

## Educational Value

This tool helps understand:
- How malicious keyloggers operate
- The importance of endpoint security
- Keystroke capture techniques
- Ethical hacking methodologies

## Defensive Measures

To protect against keyloggers:
- Use reputable antivirus software
- Enable real-time protection
- Use virtual keyboards for sensitive input
- Implement application whitelisting
- Monitor system processes regularly

**Remember: Use this tool responsibly and ethically!**
