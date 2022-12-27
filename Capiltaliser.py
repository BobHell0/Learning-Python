# Capitaliser 
str = input("Insert a phrase: ")

message = ""

num_spaces = str.count(" ")

for i in range(num_spaces):
    x = str.find(" ")
    str_i = str[0:x]
    str_i = str_i.capitalize()
    message += " " + str_i
    str = str[x+1:len(str)]

message += " " + str.capitalize()
message = message.lstrip()

print(message)





