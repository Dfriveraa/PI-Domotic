from _thread import start_new_thread
from MqttConnection import Mqtt
from SocketServer import Socket

import tensorflow as tf

mqtt = Mqtt()
socket = Socket()
try:
    start_new_thread(mqtt.start, ())
except Exception as ex:
    print("Error: unable to start thread. ex: {}".format(ex))

socket.count_back()
socket.start()
