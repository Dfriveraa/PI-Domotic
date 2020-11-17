import socket
import struct

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

socket.bind(('0.0.0.0', 8090))

while True:
    content = socket.recv(180)
    a = struct.unpack('2H6h', content)
    print(a)
