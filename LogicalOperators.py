# logical operators (and, or, not) = used to check if two or more conditional statements is true 

temp = int(input("What is the temperature outside? "))

if temp >= 65 and temp <= 78:
  print("The weather is great outside!")
elif not temp < 0 or temp > 30:
  print("Gotta stay home!!")
  print("It's great today!")