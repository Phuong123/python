# coding=utf-8
import timeit
import time
def functionA():
    print("Function A starts the execution:")
    print("Function A completes the execution:")

def functionB():
    print("Function B starts the execution")
    print("Function B completes the execution")

start_time = timeit.default_timer()
functionA()
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
functionB()
print(timeit.default_timer() - start_time)