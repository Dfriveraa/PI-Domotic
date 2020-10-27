import numpy as np
import time


def fourier(data, f_value):
    x = np.fft.rfft(data, axis=0)
    ones = np.ones(f_value)
    zeros = np.zeros(x.shape[0] - f_value)
    c = np.concatenate((ones, zeros))
    clean = x * c.reshape(x.shape[0], 1)
    x = np.fft.irfft(clean, axis=0)
    return x


def normalize(data):
    data = (data + 32762) / 65536
    return data


def filter(collection):
    data = np.array(collection)
    data = fourier(data, 30)
    data = normalize(data)
    return np.array([data])

def count_back(count):
    while count > 0:
        print(count)
        time.sleep(count)
        count -= 1