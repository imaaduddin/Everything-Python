# scope = the region that a variable is recognized 
# a varibale is only available from inside the region it is created 
# a global and locally scoped versions of a variable can be created 

name = "Levi" # this is a global scope (avilable inside and outside functions)

def display_name():
  name = "Eren" # this is local scope (avilable only inside this function)
  print(name)

print(name)