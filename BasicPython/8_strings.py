long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])

print(long_string[0:len(long_string)])

print(long_string[-15:]) #15 characters from end

print(long_string[:-15]) #Print characters except those 15 characters from end

print(long_string[:4] + " be there")

print(long_string.capitalize()) #This is will captialize first letter after fullstop

print(long_string.find("Floor"))
print(long_string.isalnum())

print(long_string.replace("Floor","Ground"))
print(long_string)


#NOTE : String are immutable

print(long_string.strip()) #Remove unwanted whitespaces
quote_list = long_string.split(" ")

print(quote_list)
