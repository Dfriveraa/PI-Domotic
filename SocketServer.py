import socket
import struct
from Gesture import Gesture
from Classifier import Classifier
from Utils import count_back

class Socket:
    """"""

    def __init__(self, ):
        self.model = Classifier()
        self.host = ('0.0.0.0', 8090)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.bind(self.host)

    def start(self):
        gesture = Gesture(self.model)
        count = 0
        while count < 300:
            content = self.socket.recv(180)
            count += 1
            print(count)
            gesture.append(struct.unpack('2H6h', content))
        gesture.predict()
