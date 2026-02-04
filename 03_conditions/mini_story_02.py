
snacks = ["cookies", "samosa"]

customer_input = input("Whats snacks do u want?: ").lower()

if customer_input in snacks:
    print("Order confirmed")
else:
    print("Snack not available")
