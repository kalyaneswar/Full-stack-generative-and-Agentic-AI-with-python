from multiprocessing import Process
import time

def brew_chai(name):
    print(f"start of {name} chai is brewing")
    time.sleep(3)
    print(f"end of {name} chai is brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
        for i in range(3)
    ]

    # start all process
    for p in chai_makers:
        p.start()

    # wait all to complete
    for p in chai_makers:
        p.join()
    
    print(f"All Chai Served")