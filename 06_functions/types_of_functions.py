# pure functions
def pure_chai(cups):
    return cups + 10

total_chai = 0

# not recomended
# impure functions
def impure_chai(cups):
    global total_chai
    total_chai += cups

# recuressive function
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))

# Lambda function

chai_types = ["kadai", "light", "ginger", "kadai"]

strong_chai = list(filter(lambda chai: chai!="kadai", chai_types))

print(strong_chai)