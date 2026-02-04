class OutOfIngredientsErrors(Exception):
    pass

def make_chai(milk, sugar):
    if milk ==0 and sugar == 0:
        raise OutOfIngredientsErrors("Missing milk or Sugar")
    print("Chai is ready ...")

make_chai(0,1)
make_chai(0,0)