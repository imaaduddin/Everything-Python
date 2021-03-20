# set = a collection which is unordered, unindexed. No duplicate values 

utensils = {"fork", "spoon", "knife"}
dishes = {"plate", "bowl", "cup"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

dinner_table = utensils.union(dishes)
# print(dishes.difference(utensils))
print(utensils.intersection(dishes))

for x in dinner_table:
  print(x)
