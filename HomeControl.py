from MqttConnection import Mqtt


class Home():
    """"""

    def __init__(self, ):
        self.tree = {
            1: {1: ("tv/channel", 'up'), 2: ("tv/channel", 'down'), 3: ("tv/state", 'on')},
            2: {1: ("light/state", 'on'), 2: ("light/state", 'off'), 3: ("light/intensity", 'up')},
            3: {1: ("thing/state", 'on'), 2: ("thing/state", 'off'),3: ("tv/state", 'on')}}
        self.state = 0
        self.one = 0
        self.two = 0

    def update(self, new):
        if new == 0:
            self.state = 0
        else:
            if self.state == 0:
                self.one = new
                self.state += 1
            else:
                self.two = new
                self.send()

    def send(self):
        print(self.tree[self.one][self.two])
        Mqtt.send_pub(self.tree[self.one][self.two][0],self.tree[self.one][self.two][1])
        self.one = 0
        self.two = 0
        self.state = 0
