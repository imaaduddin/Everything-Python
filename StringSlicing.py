# slicing = create substring by extracting elements from another string 
# indexing[] or slice()
# [start:stop:step]

# name = "Itachi Uchiha"

# first_name = name[0:3] # [0:3]
# last_name = name[7:13] # [4:end]
# funky_name = name[0:13:2] # [0:end:2]
# reversed_name = name[0:13:-1] # [0:end:-1]

# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

website = "http://google.com"
website2 = "http://apple.com"

slice = slice(7, -4)

print(website[slice])
print(website2[slice])