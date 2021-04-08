# with open("test.txt") as file:
#   print(file.read())


try:
  with open("tst.txt") as file:
    print(file.read())
except FileNotFoundError:
  print("That file was not found :(")