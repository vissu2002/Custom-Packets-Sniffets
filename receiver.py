import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Allow socket reuse
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to all interfaces on port 9998
sock.bind(('0.0.0.0', 9998))

print("Receiver Listening on port 9998...")

while True:
    data, addr = sock.recvfrom(1024)  # Proper unpacking
    print(f"Received from {addr}: {data.decode()}")  # Decode only the data part
