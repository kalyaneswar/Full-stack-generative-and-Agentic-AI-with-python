import threading
import time

def boil_milk():
    print(f"Boiling Milk ...")
    time.sleep(2)
    print(f"Milk Boiled ...")

def toast_bun():
    print(f"toasting bun...")
    time.sleep(3)
    print(f"Done with bun toast...")


# boil_milk()
# toast_bun()

start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Total time taken is  {end - start:.2f} seconds")