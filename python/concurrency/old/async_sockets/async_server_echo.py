import asyncio
import socket
from asyncio import AbstractEventLoop


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    while data := await loop.sock_recv(connection, 1024):
        print(f"I got data: {data}!")
        if data == b"boom\r\n":
            raise Exception("Unexpected network error")

        await loop.sock_sendall(connection, data)


async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Got a connection from {address}.")
        asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 8000)
    server_socket.bind(server_address)
    server_socket.setblocking(False)
    server_socket.listen()

    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())