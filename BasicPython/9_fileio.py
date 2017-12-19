
import os

test_file = open("test.txt","wb") #Append to file

print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Write Me to file\n","UTF-8"))


test_file.close()

test_file = open("test.txt","r+")

text_in_file = test_file.read()

print(text_in_file)
test_file.close()


os.remove("test.txt")
