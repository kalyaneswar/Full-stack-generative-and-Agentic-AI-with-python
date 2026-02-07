import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        print(f"Task1 accuried lock a")
        with lock_b:
            print("Task1 accuried lock b")

def task2():
    with lock_b:
        print(f"Task2 accuried lock b")
        with lock_a:
            print("Task2 accuried lock a")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()