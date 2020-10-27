import tensorflow as tf


class Classifier:

    def __init__(self):
        self.model = tf.keras.models.load_model('./ModelsTF/modelo_bs100_sf10_nf5.h5')

    def predict(self, gesture):
        class_gesture = self.model.predict(gesture).argmax(axis=1)
        return class_gesture
