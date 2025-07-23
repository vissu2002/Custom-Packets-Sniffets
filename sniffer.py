# from scapy.all import sniff,wrpcap
#
# captured_packets = []
#
# #Function to display each captured packet summary
# def packet_handler(packet):
#     print(packet.summary())
#     captured_packets.append(packet)
#
# # Capture 10 packets on default interface
# sniff(count=10,prn=packet_handler)
#
# #Save the captured packets to a pcap file
# wrpcap("captured_packets.pcap",captured_packets)
#
# print("Packets Saved to captured_packets.pcap")

from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet.proto
        length = len(packet)

        protocol_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(proto, str(proto))

        print(f"Source: {src_ip} -> Destination: {dst_ip} | Protocol: {protocol_name} | Length: {length} bytes")

print("Sniffing packets... Press Ctrl+C to stop.")
sniff(prn=process_packet, store=False, count=10)

