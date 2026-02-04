class InvalidChaiError(Exception): 
    pass

def bill(flavour, cups):
    menu = {"masala": 20, "ginger": 40}

    try:
        if flavour not in menu:
            raise InvalidChaiError("That chai not avaliable in menu")
        if not isinstance(cups, int):
            raise TypeError("No. of cups must be integer")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} of flavor {flavour} chai: rupees : {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thankyou for visting")
    
bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)
