class Chai:
    origin = "India"

print(Chai.origin)

# Properties
Chai.is_hot = True
print(Chai.is_hot)

# Creating Objects from class Chai

masala = Chai()
print(masala.origin)
print(masala.is_hot)

masala.is_hot = False

print("Class: ", Chai.is_hot)
print("masala: ", masala.is_hot)

masala.flavour = "Masala"
print(masala.flavour)