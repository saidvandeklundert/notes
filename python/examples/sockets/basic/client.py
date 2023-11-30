import socket
import sys

HOST = "127.0.0.1"
PORT = 8081

message = sys.argv[1]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(message, "utf-8"))
    data = sock.recv(1024)

print(f"Received data: {data}")
