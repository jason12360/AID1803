from signal import *
import time

def handler(sig,frame):
    print("5s")


alarm(5)
while 1:
    signal(SIGALRM,handler)
