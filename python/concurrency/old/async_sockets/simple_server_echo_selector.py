import socket
import selectors
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 8000)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)


while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)

    if len(events) == 0:
        print("no events")

    for event, _ in events:
        event_socket = event.fileobj

        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f"I got a connection from {address}")
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            print(f"I got some data: {data}")
            event_socket.send(data)
