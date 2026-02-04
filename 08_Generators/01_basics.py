def serve_chai():
    yield "Cup1: Masala Chai"
    yield "Cup2: Ginger Chai"
    yield "Cup3: Elachi Chai"

stall = serve_chai()

print(stall)
print(next(stall))
print(next(stall))
print(next(stall))

# for cup in stall:
#     print(cup)