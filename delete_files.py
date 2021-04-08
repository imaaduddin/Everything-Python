import os
import shutil

path = "test3.txt"

try:
  os.remove(path) # dlete a file 
  # os.rmdir(path) # delete an empty directory
  # shutil.rmtree(path) # delete a directory containing files
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to dlete that")
except OSError:
  print("You cannot delete that using that fucntion")
else:
  print(path + " was deleted")
