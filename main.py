from _thread import start_new_thread
from MqttConnection import Mqtt
from SocketServer import Socket
from Utils import count_back
mqtt = Mqtt()
socket = Socket()
try:
    start_new_thread(mqtt.start, ())
except Exception as ex:
    print("Error: unable to start thread. ex: {}".format(ex))

while True:
    count_back(3)
    socket.start()
