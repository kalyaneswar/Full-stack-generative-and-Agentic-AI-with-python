staff = [("kalyan", 16), ("zara", 17), ("Raj", 15)]

for name, age in staff:
    if age >= 18:
        print("Able to vote")
        break
else:
    print("Not able to vote")