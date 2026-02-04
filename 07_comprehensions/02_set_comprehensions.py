fav_chai = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elachi Chai"
]

unique_chai = {chai for chai in fav_chai if "Chai" in chai }
print(unique_chai)