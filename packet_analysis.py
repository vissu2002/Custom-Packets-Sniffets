import pandas as pd

# Load the CSV file
df = pd.read_csv("packets.csv")

# 1. Total packets
total_packets = len(df)

# 2. Protocol-wise packet count
protocol_counts = df['Protocol'].value_counts()

# 3. Top 5 Source IPs
top_src_ips = df['Source'].value_counts().head(5)

# 4. Top 5 Destination IPs
top_dst_ips = df['Destination'].value_counts().head(5)

# 5. Total bytes
total_bytes = df['Length'].sum()

# Display the results
print("========== Packet Analysis ==========")
print(f"📦 Total Packets Captured: {total_packets}")
print("\n📊 Protocol-wise Packet Count:\n", protocol_counts)
print("\n🔝 Top 5 Source IPs:\n", top_src_ips)
print("\n🔝 Top 5 Destination IPs:\n", top_dst_ips)
print(f"\n💾 Total Bytes Captured: {total_bytes} bytes")
print("======================================")
