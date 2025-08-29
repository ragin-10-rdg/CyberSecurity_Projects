#!/usr/bin/env python3
"""
Packet Sniffer Tool
Educational network packet analyzer for cybersecurity learning purposes.

ETHICAL DISCLAIMER:
This tool is designed EXCLUSIVELY for educational purposes and authorized network analysis.
- Only use on networks you own or have explicit written permission to monitor
- Unauthorized packet sniffing is illegal and unethical
- This tool should never be used for malicious purposes
- Always respect privacy and follow applicable laws
"""

import socket
import struct
import textwrap
import datetime
import os
import threading
import time

class PacketSniffer:
    def __init__(self, interface='', save_to_file=False, output_file='captured_packets.txt'):
        """
        Initialize the packet sniffer.
        
        Args:
            interface (str): Network interface to sniff on
            save_to_file (bool): Whether to save packets to file
            output_file (str): Output file for saved packets
        """
        self.interface = interface
        self.save_to_file = save_to_file
        self.output_file = output_file
        self.is_sniffing = False
        self.packet_count = 0
        self.protocols = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
        
    def create_socket(self):
        """Create and configure the raw socket."""
        try:
            # Create raw socket
            if os.name == 'nt':  # Windows
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
                sock.bind((self.interface or socket.gethostname(), 0))
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                # Enable promiscuous mode on Windows
                sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
            else:  # Linux/Unix
                sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
            
            return sock
        except PermissionError:
            print("Error: Administrator/root privileges required for packet sniffing!")
            return None
        except Exception as e:
            print(f"Error creating socket: {e}")
            return None
    
    def parse_ethernet_header(self, raw_data):
        """Parse Ethernet header (Linux only)."""
        dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])
        return {
            'dest_mac': ':'.join(f'{b:02x}' for b in dest),
            'src_mac': ':'.join(f'{b:02x}' for b in src),
            'proto': socket.htons(prototype)
        }
    
    def parse_ip_header(self, raw_data):
        """Parse IP header from raw packet data."""
        # Unpack the first 20 bytes (basic IP header)
        ip_header = struct.unpack('!BBHHHBBH4s4s', raw_data[:20])
        
        version_ihl = ip_header[0]
        version = version_ihl >> 4
        ihl = (version_ihl & 0xF) * 4
        
        ttl = ip_header[5]
        protocol = ip_header[6]
        src_addr = socket.inet_ntoa(ip_header[8])
        dest_addr = socket.inet_ntoa(ip_header[9])
        
        return {
            'version': version,
            'header_length': ihl,
            'ttl': ttl,
            'protocol': protocol,
            'src_ip': src_addr,
            'dest_ip': dest_addr
        }
    
    def parse_tcp_header(self, raw_data):
        """Parse TCP header."""
        tcp_header = struct.unpack('!HHLLBBHHH', raw_data[:20])
        
        src_port = tcp_header[0]
        dest_port = tcp_header[1]
        sequence = tcp_header[2]
        acknowledgment = tcp_header[3]
        offset_reserved = tcp_header[4]
        tcp_header_length = (offset_reserved >> 4) * 4
        
        return {
            'src_port': src_port,
            'dest_port': dest_port,
            'sequence': sequence,
            'acknowledgment': acknowledgment,
            'header_length': tcp_header_length
        }
    
    def parse_udp_header(self, raw_data):
        """Parse UDP header."""
        udp_header = struct.unpack('!HHHH', raw_data[:8])
        
        return {
            'src_port': udp_header[0],
            'dest_port': udp_header[1],
            'length': udp_header[2],
            'checksum': udp_header[3]
        }
    
    def format_payload(self, data, max_length=100):
        """Format payload data for display."""
        if len(data) > max_length:
            data = data[:max_length]
        
        # Convert to printable characters
        printable_data = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in data)
        
        # Create hex dump
        hex_data = ' '.join(f'{b:02x}' for b in data)
        
        return {
            'printable': printable_data,
            'hex': hex_data,
            'length': len(data)
        }
    
    def process_packet(self, raw_data):
        """Process and analyze a captured packet."""
        self.packet_count += 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        
        packet_info = {
            'timestamp': timestamp,
            'packet_num': self.packet_count,
            'total_length': len(raw_data)
        }
        
        try:
            # Skip Ethernet header on Linux (14 bytes)
            if os.name != 'nt':
                if len(raw_data) < 14:
                    return
                eth_header = self.parse_ethernet_header(raw_data)
                ip_data = raw_data[14:]
                packet_info['ethernet'] = eth_header
            else:
                ip_data = raw_data
            
            # Parse IP header
            if len(ip_data) < 20:
                return
                
            ip_header = self.parse_ip_header(ip_data)
            packet_info['ip'] = ip_header
            
            # Parse transport layer
            transport_data = ip_data[ip_header['header_length']:]
            protocol_name = self.protocols.get(ip_header['protocol'], f"Unknown({ip_header['protocol']})")
            packet_info['protocol'] = protocol_name
            
            if ip_header['protocol'] == 6:  # TCP
                if len(transport_data) >= 20:
                    tcp_header = self.parse_tcp_header(transport_data)
                    packet_info['tcp'] = tcp_header
                    payload_data = transport_data[tcp_header['header_length']:]
            elif ip_header['protocol'] == 17:  # UDP
                if len(transport_data) >= 8:
                    udp_header = self.parse_udp_header(transport_data)
                    packet_info['udp'] = udp_header
                    payload_data = transport_data[8:]
            else:
                payload_data = transport_data
            
            # Format payload
            if payload_data:
                packet_info['payload'] = self.format_payload(payload_data)
            
            return packet_info
            
        except Exception as e:
            print(f"Error processing packet {self.packet_count}: {e}")
            return None
    
    def display_packet(self, packet_info):
        """Display packet information."""
        if not packet_info:
            return
        
        print(f"\n{'='*80}")
        print(f"Packet #{packet_info['packet_num']} - {packet_info['timestamp']}")
        print(f"Total Length: {packet_info['total_length']} bytes")
        print(f"{'='*80}")
        
        # IP Information
        ip = packet_info.get('ip', {})
        print(f"IP: {ip.get('src_ip', 'Unknown')} -> {ip.get('dest_ip', 'Unknown')}")
        print(f"Protocol: {packet_info.get('protocol', 'Unknown')} | TTL: {ip.get('ttl', 'Unknown')}")
        
        # Transport layer information
        if 'tcp' in packet_info:
            tcp = packet_info['tcp']
            print(f"TCP: Port {tcp['src_port']} -> {tcp['dest_port']}")
            print(f"Sequence: {tcp['sequence']} | Acknowledgment: {tcp['acknowledgment']}")
        elif 'udp' in packet_info:
            udp = packet_info['udp']
            print(f"UDP: Port {udp['src_port']} -> {udp['dest_port']}")
            print(f"Length: {udp['length']} bytes")
        
        # Payload information
        if 'payload' in packet_info:
            payload = packet_info['payload']
            print(f"\nPayload ({payload['length']} bytes):")
            print(f"Printable: {payload['printable'][:50]}{'...' if len(payload['printable']) > 50 else ''}")
            print(f"Hex: {payload['hex'][:50]}{'...' if len(payload['hex']) > 50 else ''}")
    
    def save_packet(self, packet_info):
        """Save packet information to file."""
        if not self.save_to_file or not packet_info:
            return
        
        try:
            with open(self.output_file, 'a', encoding='utf-8') as f:
                f.write(f"\nPacket #{packet_info['packet_num']} - {packet_info['timestamp']}\n")
                f.write(f"Length: {packet_info['total_length']} bytes\n")
                
                ip = packet_info.get('ip', {})
                f.write(f"IP: {ip.get('src_ip', 'Unknown')} -> {ip.get('dest_ip', 'Unknown')}\n")
                f.write(f"Protocol: {packet_info.get('protocol', 'Unknown')}\n")
                
                if 'tcp' in packet_info:
                    tcp = packet_info['tcp']
                    f.write(f"TCP: {tcp['src_port']} -> {tcp['dest_port']}\n")
                elif 'udp' in packet_info:
                    udp = packet_info['udp']
                    f.write(f"UDP: {udp['src_port']} -> {udp['dest_port']}\n")
                
                if 'payload' in packet_info:
                    payload = packet_info['payload']
                    f.write(f"Payload: {payload['printable'][:100]}\n")
                
                f.write("-" * 80 + "\n")
        except Exception as e:
            print(f"Error saving packet: {e}")
    
    def start_sniffing(self, packet_limit=0, protocol_filter=None):
        """
        Start packet sniffing.
        
        Args:
            packet_limit (int): Maximum number of packets to capture (0 = unlimited)
            protocol_filter (str): Protocol to filter ('TCP', 'UDP', 'ICMP', or None)
        """
        print("=" * 60)
        print("ETHICAL DISCLAIMER:")
        print("This packet sniffer is for educational purposes only.")
        print("Only use on networks you own or have permission to monitor.")
        print("Unauthorized packet sniffing is illegal!")
        print("=" * 60)
        
        confirm = input("Do you understand and agree? (yes/no): ").lower().strip()
        if confirm != 'yes':
            print("Packet sniffer not started. Ethical agreement required.")
            return
        
        sock = self.create_socket()
        if not sock:
            return
        
        self.is_sniffing = True
        self.packet_count = 0
        
        print(f"\nStarting packet capture...")
        print(f"Interface: {self.interface or 'Default'}")
        print(f"Protocol filter: {protocol_filter or 'All'}")
        print(f"Packet limit: {packet_limit or 'Unlimited'}")
        print(f"Save to file: {self.save_to_file}")
        if self.save_to_file:
            print(f"Output file: {self.output_file}")
        print("Press Ctrl+C to stop\n")
        
        try:
            while self.is_sniffing:
                raw_data, addr = sock.recvfrom(65536)
                
                packet_info = self.process_packet(raw_data)
                if packet_info:
                    # Apply protocol filter
                    if protocol_filter and packet_info.get('protocol') != protocol_filter:
                        continue
                    
                    self.display_packet(packet_info)
                    self.save_packet(packet_info)
                    
                    # Check packet limit
                    if packet_limit > 0 and self.packet_count >= packet_limit:
                        print(f"\nReached packet limit ({packet_limit}). Stopping...")
                        break
        
        except KeyboardInterrupt:
            print("\nPacket capture interrupted by user.")
        except Exception as e:
            print(f"Error during packet capture: {e}")
        finally:
            self.stop_sniffing()
            sock.close()
    
    def stop_sniffing(self):
        """Stop packet sniffing."""
        self.is_sniffing = False
        print(f"\nPacket capture stopped. Total packets captured: {self.packet_count}")
        if self.save_to_file:
            print(f"Packets saved to: {self.output_file}")

def main():
    """Main function to run the packet sniffer tool."""
    print("=" * 60)
    print("         EDUCATIONAL PACKET SNIFFER TOOL")
    print("=" * 60)
    print("WARNING: This tool is for educational purposes only!")
    print("Only use on networks you own or have explicit permission to monitor.")
    print("Unauthorized packet sniffing is illegal and unethical.")
    print("=" * 60)
    
    sniffer = PacketSniffer()
    
    while True:
        print("\nChoose an option:")
        print("1. Start packet sniffing")
        print("2. Configure settings")
        print("3. View saved packets")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Get sniffing parameters
            try:
                packet_limit = int(input("Enter packet limit (0 for unlimited): ") or "0")
            except ValueError:
                packet_limit = 0
            
            protocol_filter = input("Enter protocol filter (TCP/UDP/ICMP or leave empty): ").strip().upper()
            if protocol_filter not in ['TCP', 'UDP', 'ICMP']:
                protocol_filter = None
            
            sniffer.start_sniffing(packet_limit, protocol_filter)
        
        elif choice == '2':
            print("\nCurrent settings:")
            print(f"Interface: {sniffer.interface or 'Default'}")
            print(f"Save to file: {sniffer.save_to_file}")
            print(f"Output file: {sniffer.output_file}")
            
            # Configure interface
            new_interface = input("Enter network interface (leave empty for default): ").strip()
            sniffer.interface = new_interface
            
            # Configure file saving
            save_choice = input("Save packets to file? (y/n): ").lower().strip()
            sniffer.save_to_file = save_choice == 'y'
            
            if sniffer.save_to_file:
                new_file = input("Enter output filename (default: captured_packets.txt): ").strip()
                if new_file:
                    sniffer.output_file = new_file
            
            print("Settings updated!")
        
        elif choice == '3':
            if os.path.exists(sniffer.output_file):
                try:
                    lines = int(input("Number of recent lines to view (default 50): ") or "50")
                    with open(sniffer.output_file, 'r', encoding='utf-8') as f:
                        all_lines = f.readlines()
                    
                    print(f"\n--- Last {min(lines, len(all_lines))} lines from {sniffer.output_file} ---")
                    for line in all_lines[-lines:]:
                        print(line.strip())
                except Exception as e:
                    print(f"Error reading file: {e}")
            else:
                print("No saved packets file found!")
        
        elif choice == '4':
            print("Thank you for using Educational Packet Sniffer Tool!")
            print("Remember: Use technology ethically and responsibly!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
