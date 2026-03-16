# CodeAlpha_Basic-NetworkSniffer
Basic Packet Sniffer
Project Description

This project is a basic network packet sniffer developed using Python.
The program captures network packets and displays useful information such as source IP address, destination IP address, protocol type, port numbers, and packet payload.

It helps in understanding how data travels across a network and how network protocols work.

Objectives
Capture network traffic packets.
Analyze packet structure and contents.
Understand the flow of data in a network.
Learn the basics of network protocols.

Technologies Used
Python
Scapy (for packet capturing and analysis)

Features
Captures live network packets.
Displays source and destination IP addresses.
Identifies TCP and UDP protocols.
Shows source and destination ports.
Displays packet payload data.

Installation
Install the required library before running the program:
pip install scapy

How to Run the Program
Clone the repository from GitHub
git clone https://github.com/yourusername/basic-packet-sniffer.git

Navigate to the project folder
cd basic-packet-sniffer

Run the program
python packet_sniffer.py

(In Linux you may need root permissions)

sudo python3 packet_sniffer.py

Example Output
Packet Captured
Source IP: 192.168.1.10
Destination IP: 142.250.183.14
Protocol: TCP
Source Port: 52000
Destination Port: 443
Payload: GET / HTTP/1.1

Learning Outcomes
Understanding of packet capturing.
Basic knowledge of network protocols.
Practical experience with network analysis tools.

Future Improvements
Add support for HTTP and DNS protocol detection.
Save captured packets to a file.
Create a GUI-based packet analyzer.
