from scapy.all import sniff, IP, TCP, UDP, Raw

# Function to analyze packets
def analyze_packet(packet):

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n--- Packet Captured ---")
        print("Source IP:", src_ip)
        print("Destination IP:", dst_ip)
        print("Protocol:", protocol)

        # Check for TCP
        if packet.haslayer(TCP):
            print("Protocol Type: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        # Check for UDP
        elif packet.haslayer(UDP):
            print("Protocol Type: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        # Payload
        if packet.haslayer(Raw):
            print("Payload:", packet[Raw].load)

# Capture packets
print("Starting packet capture... Press Ctrl+C to stop")

sniff(prn=analyze_packet, count=10)
