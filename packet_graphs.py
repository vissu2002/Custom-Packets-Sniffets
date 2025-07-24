import pandas as pd
import matplotlib.pyplot as plt

# Read packet data
df = pd.read_csv("packets.csv")

#Packet Distribution
protocol_counts = df['Protocol'].value_counts()

plt.figure(figsize=(8, 6))
protocol_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title(" Protocol Usage Distribution")
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("protocol_distribution.png")  # Save image
plt.show()

#Top 5 source IP's
top_src_ips = df['Source'].value_counts().head(5)

plt.figure(figsize=(8, 6))
top_src_ips.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title("Top 5 Source IPs")
plt.xlabel("Source IP")
plt.ylabel("Packet Count")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("top_source_ips.png")  # Save image
plt.show()

#Top 5 Destination IP's
top_dst_ips = df['Destination'].value_counts().head(5)

plt.figure(figsize=(8, 6))
top_dst_ips.plot(kind='bar', color='salmon', edgecolor='black')
plt.title("🔝 Top 5 Destination IPs")
plt.xlabel("Destination IP")
plt.ylabel("Packet Count")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("top_destination_ips.png")  # Save image
plt.show()

