import tensorflow as tf
import os
import numpy as np


class Classifier:

    def __init__(self):
        names = os.listdir('./ModelsTF/mejores2')
        self.models = []
        for i in names:
            self.models.append(tf.keras.models.load_model('./ModelsTF/mejores2/' + i))

    def predict(self, gesture):
        a = np.empty(shape=[0, 4])
        for model in self.models:
            result = model.predict(gesture)
            a = np.append(a, result, axis=0)
        class_gesture = np.sum(a, axis=0)
        class_gesture = class_gesture / len(self.models)
        label = class_gesture.argmax()
        if class_gesture[label] > 0.9:
            return label
        else:
            return 1
