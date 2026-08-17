import threading, time, random

BUFFER_SIZE = 5
buffer = [None] * BUFFER_SIZE
in_idx = 0

mutex = threading.Semaphore(1)
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

def producer():
    global in_idx
    for i in range(1, 11):
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        
        buffer[in_idx] = item
        print(f"Produced {item} at {in_idx} | Buffer: {buffer}")
        in_idx = (in_idx + 1) % BUFFER_SIZE
        
        mutex.release()
        full.release()
        time.sleep(0.1)

if __name__ == "__main__":
    t1 = threading.Thread(target=producer)
    t1.start()
    t1.join()
