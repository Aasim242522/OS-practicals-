from multiprocessing import Process, Queue
import time, random

def producer(q):
    for i in range(10): # Increased range to observe blocking
        item = random.randint(1, 100)
        q.put(item) # Blocks if queue size is 3
        print(f"Produced: {item}")
        time.sleep(0.5)

def consumer(q):
    while True:
        item = q.get() # Blocks if queue is empty
        print(f"Consumed: {item}")
        time.sleep(1.5) # Slower consumer to force queue to fill up

if __name__ == "__main__":
    q = Queue(maxsize=3) # Limit queue to 3 items
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start(); p2.start()
    p1.join(); p2.join()
