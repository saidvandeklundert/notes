import socket
import time


HOST = socket.gethostbyname(socket.gethostname())


s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)


# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)


ip_header = b"\x45\x00\x00\x1c"  # Version, IHL, Type of Service | Total Length
ip_header += b"\xab\xcd\x00\x00"  # Identification | Flags, Fragment Offset
ip_header += b"\x40\x01\x6b\xd8"  # TTL, Protocol | Header Checksum
ip_header += b"\xc0\xa8\x1e\x15"  # Source Address
ip_header += b"\x08\x08\x08\x08"  # Destination Address

icmp_header = b"\x08\x00\xe5\xc9"  # Type of message, Code | Checksum
icmp_header += b"\x12\x34\x00\x02"  # Identifier | Sequence Number

packet = ip_header + icmp_header
# s.sendto(packet, ("192.168.1.1", 0))


for _ in range(1):
    time.sleep(0.1)
    s.sendto(packet, ("8.8.8.8", 0))
