def infinate_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinate_chai()

for _ in range(3):
    print(next(refill))