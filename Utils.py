import numpy as np
import time


def fourier(data, f_value):
    x = np.fft.rfft(data, axis=0)
    # ones = np.ones(f_value)
    # zeros = np.zeros(x.shape[0] - f_value)
    # c = np.concatenate((ones, zeros))
    e = np.linspace(30 - f_value, -30 - f_value, x.shape[0])
    e = (1 / (1 + np.exp(-e)))
    clean = x * e.reshape(x.shape[0], 1)
    x = np.fft.irfft(clean, axis=0)
    return x


def normalize(data):
    data = (data + 32762) / 65536
    return data


def extender(signal, n):
    delante = np.ones((int(n / 2), 6))
    atras = np.ones(((int(n / 2)) + (n % 2), 6))
    delante = delante * signal[0, :]
    atras = atras * signal[-1:, :]
    a = np.insert(signal, 0, delante, axis=0)
    a = np.insert(a, -1, atras, axis=0)
    return a


def filter(collection):
    data = np.array(collection)
    data = fourier(data, 20)
    data = normalize(data)
    data = extender(data, 300 - data.shape[0])
    return np.array([data])


def count_back(count):
    while count > 0:
        print(count)
        time.sleep(count)
        count -= 1
    print('ya')
