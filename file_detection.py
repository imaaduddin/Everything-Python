import os

path = "C: //Users//imaaduddin//documents//Python Code Bros"

if os.path.exists(path):
  print("This location exists!")
  if os.path.isfile(path):
    print("This is a file")
  elif os.path.isdir(path):
    print("This is a directory!")
else:
  print("That location doesn't exist")