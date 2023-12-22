from time import sleep
from threading import Thread

def imprime():
    count = 0
    while True:
        count += 1
        print(count)
        sleep(1)

t = Thread(target=imprime)
t.start()
