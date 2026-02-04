# Dict
chai_order = dict(type="Masala chai", size="Large", sugar =2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "Black Tea"
chai_recipe["Liquid"] = "Milk"
print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe : {chai_recipe}")

del chai_recipe["Liquid"]
print(f"Recipe : {chai_recipe}")

print(f"is sugar in order? {'sugar' in chai_order}")

chai_order = {"type":"Masala chai", "size":"Medium", "sugar" :1}
print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")