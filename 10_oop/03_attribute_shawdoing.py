class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"

print("After Changing ", cutting.temperature)
print("Before Changing ", Chai.temperature)
print("Cup size is ", cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
print(cutting.temperature)

del cutting.cup
print(cutting.cup)