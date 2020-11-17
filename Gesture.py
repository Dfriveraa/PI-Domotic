from Data import Data
from Utils import filter
from HomeControl import Home


# start_time = timeit.default_timer()
# self.test_clean()
# print(timeit.default_timer() - start_time)

class Gesture:
    def __init__(self, model):
        self.collection = []
        self.resume = []
        self.model = model
        self.home = Home()

    def append(self, data: tuple):
        dt = Data(data)
        self.collection.append(dt.get_all_atr())
        if len(self.collection) == 180:
            self.home.update(self.predict())
            self.collection = self.collection[60:]

    def predict(self):
        aux = filter(self.collection)
        aux = self.model.predict(aux)
        print(aux)
        return aux
