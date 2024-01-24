from time import sleep
from threading import *

class Hello():
    def run(self):
        for i in range (5):
            print("Hello")

class Hi():
    def run(self):
        for i in range (5):
            print("Hi")

h1 = Hello()
h2 = Hi()

h1.run()
h2.run()