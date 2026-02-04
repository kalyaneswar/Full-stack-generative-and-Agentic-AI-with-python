# file = open("order.txt", "w")
# try:
#     file.write("MasALA chai 2 cups")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("2 cups of masala chai")