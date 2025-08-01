import socket
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
target_ip = "127.0.0.1"
target_port = 9998

print("Sending Packets to receiver.....")

while True:
    message = "Hello from sender"
    sock.sendto(message.encode(),(target_ip,target_port))
    print(f"Sent:{message}")
    time.sleep(2)

    
