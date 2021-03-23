# keyword arguments = arguments preceded by an identifier when we pass them to a function
# the order of the arguments doesn't matter, unlike positional arguments
# Python knows the names of the arguments that our function receives 

def greeting(first, middle, last):
  print("Hello " + first + " " + middle + " " + last)

greeting(last="Yo", first="Haha", middle="Hehe")
