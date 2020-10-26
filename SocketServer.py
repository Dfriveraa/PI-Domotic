import socket
import struct

import time


class Socket:
    """"""

    def __init__(self, ):
        self.host = ('0.0.0.0', 8090)
        self.count = 3
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    def count_back(self):
        while self.count > 0:
            print(self.count)
            time.sleep(self.count)
            self.count -= 1

    def start(self):
        self.socket.bind(self.host)
        count=0
        while count < 300:
            content = self.socket.recv(180)
            count = count + 1
            # gesture.append(struct.unpack('2H6h', content))