import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)

connections = []

try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f"I got a connection from {client_address}!")
            connections.append(connection)
        except BlockingIOError:
            pass

        for connection in connections:
            buffer = connection.recv(2)
            print(f"I got data: {buffer}!")

            while buffer[-2:] != b"\r\n":
                data = connection.recv(2)
                print(f"I god data: {data}!")
                buffer = buffer + data

            print(f"All the data is : {buffer}")

            connection.send(buffer)
finally:
    server_socket.close()
