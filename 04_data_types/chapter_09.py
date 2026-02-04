# set
set1 = {"apple", "tea", "coffee"}
set2 = {"bannana", "tea", "orange"}

# union
all_set = set1 | set2
print(f"all spices: {all_set}")

# Intersection
all_set = set1 & set2
print(f"common spices: {all_set}")

only_essentioal_set1 = set1 - set2
print(f"Only essential: {only_essentioal_set1}")

print(f"is 'coffee' in set2 ? {'coffee' in set2}")