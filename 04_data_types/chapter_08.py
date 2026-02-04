ingredients = ["water", "powder", "milk"]
ingredients.append("sugar")
print(f"Current Ingredients { ingredients }")

ingredients.remove("water")
print(f"Current Ingredients { ingredients }")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["milk", "water"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")