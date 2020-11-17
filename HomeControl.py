from MqttConnection import Mqtt


class Home():
    """
    0 activacion
    1 encender (ignorado)
    2 complejon
    3 X
    """

    def __init__(self, ):
        self.tree = {
            0: {0: ("tv", '3'), 2: ("tv", '2'), 3: ("tv", '1')},
            2: {0: ("light/state", 'on'), 2: ("light/state", 'off'), 3: ("light/intensity", 'up')},
            3: {0: ("thing/state", 'on'), 2: ("thing/state", 'off'), 3: ("thin/state", 'on')}}
        self.state = 1
        self.one = 1
        self.two = 1

    # def update(self, new):
    #     if new == 0:
    #         self.state = 0
    #     else:
    #         if self.state == 0:
    #             self.one = new
    #             self.state += 1
    #         else:
    #             self.two = new
    #             self.send()

    def update(self, new):
        if new != 1 and new != self.one:
            if self.state == 1:
                self.one = new
                self.state += 1
            else:
                self.two = new
                self.send()

    def send(self):
        print(self.tree[self.one][self.two])
        Mqtt.send_pub(self.tree[self.one][self.two][0], self.tree[self.one][self.two][1])
        self.one = 1
        self.two = 1
        self.state = 1
