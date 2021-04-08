import os

source = "test2.txt"
destination = "C: //Users//imaaduddin//documents"

try:
  if os.path.exists(destination):
    print("There is already a file there")
  else:
    os.replace(source, destination)
    print(source + " was moved")
except FileNotFoundError:
  print(source + " was not found")

