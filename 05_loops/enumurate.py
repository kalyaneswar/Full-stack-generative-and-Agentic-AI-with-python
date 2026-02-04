menu = ["green", "lemon", "spice", "mint"]

for idx, item in enumerate(menu):
    print(f"for index {idx} the menu is {item}")

for idx, item in enumerate(menu, start=1):
    print(f"for index {idx} the menu is {item}")