from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range (5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range (5):
            print("Hi")
            sleep(1)

h1 = Hello()
h2 = Hi()

h1.start()
sleep(0.5)
h2.start()

print('Close')