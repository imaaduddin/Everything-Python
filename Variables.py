# Variable is a container for a value. Behaves as the value that it conatins 

first_name = "Imaad" # This is a string 
last_name= "Uddin"
full_name = first_name + " " + last_name
print("Hello " + full_name)

age = 21 # this is an int data type 
age = age + 1
print(type(age))
print("Your age is " + str(age)) # you cannot concatenate string with an int, the int would have to be changed to a string

height = 250.5 # this is a float 
print(type(height))
print("Your height is: " + str(height))

human = True # this is a boolean
print(human)
print(type(human))
print("Are you a human? " + str(human))