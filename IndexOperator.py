# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "Kakashi Hatake!!"

# if (name[0].isupper()):
#   name = name.lower()

first_name = name[0:3].upper()
last_name = name[7:].upper()
last_char = name[-2]

print(first_name)
print(last_name)
print(last_char)