# coding=utf-8
import os

def child():
    n = os.fork()
    if n > 0:
        print("PID of Parent process is : ", os.getpid())
    else:
        print("PID of Child process is : ", os.getpid())

child()