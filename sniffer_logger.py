from scapy.all import sniff, IP, TCP, UDP, ICMP
import csv
from datetime import datetime

def packet_callback(pkt):
    if IP in pkt:
        proto = "OTHER"
        if pkt.haslayer(TCP):
            proto = "TCP"
        elif pkt.haslayer(UDP):
            proto = "UDP"
        elif pkt.haslayer(ICMP):
            proto = "ICMP"

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        src = pkt[IP].src
        dst = pkt[IP].dst
        length = len(pkt)

        with open("packets.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, src, dst, proto, length])

        print(f"[{timestamp}] {src} -> {dst} | {proto} | {length} bytes")

# Write header before sniffing starts
with open("packets.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Source", "Destination", "Protocol", "Length"])

print("Sniffing... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)








