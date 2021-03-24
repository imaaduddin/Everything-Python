# str.format() = optional method that gives users more control when displaying output

character = "Zabuza"
weapon = "execution blade"

print("{} weilds the {}".format(character, weapon))

print("{0} weilds the {1}".format(character, weapon))

# print("{} weilds the {}".format(character = "Naruto", weapon = "kunai"))

text = "The {} jumped over the {}"
text.format(character, weapon)

numbers = 1000

print("The number PI is {}".format(numbers))