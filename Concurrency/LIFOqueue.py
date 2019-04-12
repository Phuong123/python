# coding=utf-8
import threading
import queue
import random
import time

def myqueue(queue):
    while not queue.empty():
        item = queue.get()
        if item is None:
            break

        print("{} removed {} from the queue".format(threading.current_thread(), item))

        queue.task_done()
        time.sleep(2)

# create a queue
q = queue.LifoQueue()
for i in range(5):
    q.put(i)


# use multiple threads
threads = []
for i in range(4):
    thread = threading.Thread(target=myqueue, args=(q,))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()