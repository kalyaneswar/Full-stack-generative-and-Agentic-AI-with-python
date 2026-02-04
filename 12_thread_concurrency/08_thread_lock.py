import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1

threds = [ threading.Thread(target=increment) for _ in range(10)]
[t.start()  for t in threds]
[t.join()  for t in threds]

print(f"Final counter is: {counter}")