import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ("localhost", 8000)
server_socket.bind(address)
server_socket.listen()
connection, client_address = server_socket.accept()
print(f"I got a connection from {client_address}!")
