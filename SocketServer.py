import socket
import struct
from Gesture import Gesture
from Classifier import Classifier
import time
import timeit


class Socket:

    def __init__(self, ):
        self.model = Classifier()
        self.host = ('0.0.0.0', 8090)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.lock = False

    def interrupt(self, count):
        while count > 0:
            print(count)
            time.sleep(count)
            count -= 1
        self.lock = False

    def start(self):
        self.socket.bind(self.host)
        while True:
            gesture = Gesture(self.model)
            count = 0
            while count < 300:
                content = self.socket.recv(180)
                count += 1
                # print(count)
                gesture.append(struct.unpack('2H6h', content))
            gesture.predict()
            start_time = timeit.default_timer()
            self.test_clean()
            print(timeit.default_timer() - start_time)
            # self.lock = True
            # self.interrupt(3)
            # cleaner = threading.Thread(target=self.clear_buffer()).start()

    def clear_buffer(self):

        try:
            while self.recv(1024) and self.lock == True: pass
        except:
            pass

    def test_clean(self):
        count = 0
        while count < 300:
            self.socket.recv(180)
            count += 1
        print('ya')
