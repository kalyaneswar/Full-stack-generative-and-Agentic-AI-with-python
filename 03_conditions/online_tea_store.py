
amount = 0
delivery_fee = 0
order_amount = int(input("Whats the order amount: "))
print(order_amount)
if order_amount > 300:
    print("No delivery fee")
    amount = (order_amount)
    
else:
    delivery_fee += 30
    amount = (order_amount + delivery_fee)
    print(amount)
print(amount)

# del_fee = 0 if order_amount > 300 else 30