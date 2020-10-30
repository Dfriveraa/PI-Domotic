import threading
import time
import timeit

lock = False;


class Hilo:
    def __init__(self):
        self.lock = True

    def worker(self):
        time.sleep(3)
        self.lock = False
        print('FIn del hilo')


def my_service():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.3)
    print(threading.current_thread().getName(), 'Exiting')


hilo = Hilo()
t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=hilo.worker)  # use default name

# w.start()
# t.start()
start_time = timeit.default_timer()
# w2.start()
while not hilo.lock:
    print(hilo.lock)
print(timeit.default_timer() - start_time)
