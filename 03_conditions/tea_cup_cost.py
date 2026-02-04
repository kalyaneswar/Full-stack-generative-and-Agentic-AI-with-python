cup_size = input("Please choose cup size in small, medium, large: ").lower()
cost_per_cup = {
    "small": 10,
    "mediumas": 15,
    "large": 20
}

if cup_size in cost_per_cup:
    print(f"The final amount for chai is: Rs:{cost_per_cup[cup_size]}")
else:
    print("Unknow cup size")