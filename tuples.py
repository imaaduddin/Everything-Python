# tuple = collection which is ordered and unchangable used to group together related data 

student = ("Rock Lee", 15, "male")

print(student.count("Rock Lee"))
print(student.index(15))

for x in student:
  print(x)

if "Rock Lee" in student:
  print("Lee is here!")