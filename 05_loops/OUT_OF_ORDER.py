flavours = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Tulsi"]

for flav in flavours:
    if flav == "Out of stock":
        continue
    if flav == "Discontinued":
        print(f"{flav} item found")
        break
    print(f"{flav} item not found")

print(f"Outside of loop")