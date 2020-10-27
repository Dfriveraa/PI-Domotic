from Data import Data
from Utils import filter


class Gesture:
    def __init__(self,model):
        self.collection = []
        self.resume = []
        self.model = model

    def append(self, data: tuple):
        dt = Data(data)
        self.collection.append(dt.get_all_atr())

    def predict(self):
        aux = filter(self.collection)
        print(self.model.predict(aux))
