import threading
import time

BUFFER_SIZE = 5
# Pre-populate the buffer so the consumer has items to consume
buffer = [101, 102, 103, 104, 105]
out_idx = 0

mutex = threading.Semaphore(1)
empty = threading.Semaphore(0)  # No empty slots initially
full = threading.Semaphore(BUFFER_SIZE)  # Buffer is full

def consumer():
    global out_idx
    for i in range(1, 6):
        full.acquire()    # Wait for a filled slot
        mutex.acquire()   # Enter critical section
        
        item = buffer[out_idx]
        buffer[out_idx] = None
        print(f"Consumed {item} from {out_idx} | Buffer: {buffer}")
        out_idx = (out_idx + 1) % BUFFER_SIZE
        
        mutex.release()   # Exit critical section
        empty.release()   # Signal an empty slot
        time.sleep(0.2)

if __name__ == "__main__":
    t2 = threading.Thread(target=consumer)
    t2.start()
    t2.join()
