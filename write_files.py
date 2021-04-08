text = "Hello, this is some text. Just adding to the text file."

with open("testing.txt", "a") as file:
  file.write(text)