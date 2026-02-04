def chai_customter():
    print("Welcome to the chai world! what chai do u like to have")
    order = yield
    while True:
        print(f"Preparing : {order}")
        order = yield

stall = chai_customter()
next(stall) #start the genrator

stall.send("Masala chai")
stall.send("Masala chai2")