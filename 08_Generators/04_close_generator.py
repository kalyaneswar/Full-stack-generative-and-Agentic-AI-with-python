def local_chai():
    yield "Masala Chai"
    yield "Ginger chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for Chai order"
    except:
        print("Stall closed")

stall = chai_stall()
print(next(stall))
stall.close() # not only close but also clean up memory
