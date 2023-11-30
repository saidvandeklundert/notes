import socket

HOST = "127.0.0.1"
PORT = 8081
try:
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((HOST, PORT))
            sock.listen()
            conn, addr = sock.accept()

            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)

                    if not data:
                        break
                    string = data.decode("utf-8")

                    conn.sendall(bytes(string.upper(), "utf-8"))
except KeyboardInterrupt:
    print("server halted")


import ipaddress

s = """'\r\n*************************************************************\r\n\r\nThis system is for authorized use only. It is\r\nmonitored to detect improper use and other illicit activity.\r\nThere is no expectation of privacy while using this system.\r\n\r\n*************************************************************\r\n\r\nThis device is a part of the FFNX network architecture and\r\nall configuration is strictly managed through Imperium. Engage\r\nOpsTech-Networks or CNE for any changes required.\r\n\r\n*************************************************************\r\n\r\n\r\n\r\n\r\nType escape sequence to abort.\r\nSending 1, 100-byte ICMP Echos to 205.251.242.103, timeout is 2 seconds:\r\n.\r\nSuccess rate is 0 percent (0/1)'"""

s.split()


for item in s.replace(",", " ").split():
    try:
        res = ipaddress.ip_address(item)
        if isinstance(res, ipaddress.IPv6Address):
            print("success")
        elif isinstance(res, ipaddress.IPv4Address):
            print("success")
    except ValueError:
        pass


[ipaddress.ip_address(item) for item in s.split()]
