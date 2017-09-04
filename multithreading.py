import threading
import time

print('Hi there')

# only use local variables in multithreaded target functions


def nap(t):
    time.sleep(2)
    print('Awake!', t)


threadObj = threading.Thread(target=nap, args=[time.time()])
threadObj.start()

print('Last Line')
