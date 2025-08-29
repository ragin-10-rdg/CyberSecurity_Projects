# Packet Sniffer Tool

An educational network packet analyzer for cybersecurity learning and authorized network analysis.

## ⚠️ ETHICAL DISCLAIMER

**THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY**

- Only use on networks you **own** or have **explicit written permission** to monitor
- Unauthorized packet sniffing is **illegal** and **unethical**
- Never use this tool for malicious purposes
- Always respect privacy and follow applicable laws
- Intended for cybersecurity education and authorized network analysis

## Purpose

This tool demonstrates network packet analysis concepts and helps understand:
- Network protocol structures (TCP/UDP/ICMP)
- Packet capture techniques
- Network traffic analysis
- The importance of network security monitoring

## Features

- **Real-time packet capture** with detailed analysis
- **Protocol filtering** (TCP, UDP, ICMP)
- **IP header parsing** with source/destination information
- **Transport layer analysis** (TCP/UDP headers)
- **Payload inspection** with hex and ASCII display
- **Packet logging** to text files
- **Configurable capture limits**
- **Cross-platform support** (Windows/Linux)

## How to Run

### Prerequisites
- **Administrator/Root privileges required** for raw socket access
- Python 3.6 or higher

### Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Navigate to the PacketSniffer directory

3. Run with administrator privileges:
   ```bash
   # Windows (Run as Administrator)
   python packet_sniffer.py
   
   # Linux/macOS (Run with sudo)
   sudo python3 packet_sniffer.py
   ```

## Dependencies

- **scapy**: Advanced packet manipulation library (optional alternative)
- Uses Python standard library for core functionality

## Usage Instructions

### Basic Packet Capture
1. Run the script with admin privileges
2. Choose option 1 to start sniffing
3. Accept the ethical disclaimer
4. Set packet limit (0 for unlimited)
5. Choose protocol filter (optional)
6. View real-time packet analysis

### Configuration Options
- **Interface**: Specify network interface
- **Protocol Filter**: TCP, UDP, ICMP, or all
- **Packet Limit**: Maximum packets to capture
- **File Logging**: Save packets to text file

### Sample Output
```
================================================================================
Packet #1 - 2024-08-29 13:06:15.123
Total Length: 74 bytes
================================================================================
IP: 192.168.1.100 -> 8.8.8.8
Protocol: UDP | TTL: 64
UDP: Port 53 -> 53
Length: 54 bytes

Payload (34 bytes):
Printable: .....google.com.....
Hex: 03 77 77 77 06 67 6f 6f 67 6c 65 03 63 6f 6d 00
```

## Security Considerations

### Privileges Required
- **Windows**: Run as Administrator
- **Linux/macOS**: Run with sudo
- Raw socket access needed for packet capture

### Legal Compliance
- Ensure proper authorization before use
- Document testing activities
- Follow organizational policies
- Comply with local privacy laws

### Detection Avoidance
- Modern security tools may detect packet sniffing
- Use only on authorized networks
- Be aware of network monitoring policies

## Educational Value

This tool helps understand:
- Network protocol stack operation
- Packet structure and headers
- Traffic analysis techniques
- Network security monitoring
- Ethical hacking methodologies

## Defensive Measures

To protect against packet sniffing:
- Use encrypted protocols (HTTPS, SSH, VPN)
- Implement network segmentation
- Monitor for suspicious network activity
- Use switched networks instead of hubs
- Deploy network intrusion detection systems

## Troubleshooting

### Common Issues
- **Permission Denied**: Run with admin/root privileges
- **Socket Error**: Check network interface availability
- **No Packets Captured**: Verify network activity and interface

### Platform-Specific Notes
- **Windows**: May require firewall exceptions
- **Linux**: Requires root access for raw sockets
- **Virtual Machines**: May have limited network access

**Remember: Use this tool responsibly and ethically!**
