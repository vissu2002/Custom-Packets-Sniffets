from scapy.all import sniff
from sniffer import capture_packets
import csv

def capture_packets(packet_count=10):
    with open("packet.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Source", "Destination", "Protocol", "Length"])




        def process(packet):
            writer.writerow([
                packet.time,
                packet[0].src if hasattr(packet[0], "src") else "N/A",
                packet[0].dst if hasattr(packet[0], "dst") else "N/A",
                packet.summary().split()[0],
                len(packet)
            ])

        sniff(prn=process, count=packet_count)

if __name__ == "__main__":
    capture_packets(10)
