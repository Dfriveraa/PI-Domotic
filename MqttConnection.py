import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

MQTT_LOCAL_SERVER = "localhost"
MQTT_PATH = "home"


class Mqtt:

    def __init__(self):
        self.server = "localhost"
        self.topic = "home"
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.server, 1883, 60)

    def start(self):
        self.client.loop_forever()

    @staticmethod
    def send_pub(subtopic, conf):
        try:
            print(MQTT_PATH + "/" + subtopic, "conf:" + conf)
            publish.single(MQTT_PATH + "/" + subtopic,conf, hostname=MQTT_LOCAL_SERVER)
        except Exception as ex:
            print("Error in send_conf(). ex: {}".format(ex))

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe(MQTT_PATH + "/+")

    def on_message(self, client, userdata, msg):
        print('')