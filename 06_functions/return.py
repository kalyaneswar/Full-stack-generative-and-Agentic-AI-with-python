def make_chai():
    return "Here ur Masala Chai"

return_value = make_chai()

print(return_value)


def sold_cups():
    return 123

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Chai! over"
    return "Chai is ready"

print(chai_status(0))
print(chai_status(5))

def chai_repot():
    return 23, 43

sold, remaining = chai_repot()
print("Sold", sold)
print("Remaing", remaining)