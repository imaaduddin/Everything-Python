# dictionary = a changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly 

capitals = {
  "USA" : "Washington D.C",
  "India" : "New Delhi",
  "China" : "Beijing",
  "Russia" : "Moscow"
}

capitals.update({"Germany" : "Berlin"})
capitals.update({"USA" : "New York City"})
capitals.pop("Russia")
capitals.clear()

# print(capitals["Russia"])
# print(capitals.get("England"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
  print(key, value)