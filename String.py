name = "Bhanu"
print("Hello, " + name)

friend = 'Deepu' # we can also use single quotes
print(friend)

print('He said, "I want to eat an apple".')

# *******multiple string*********
a = '''Hlw
My name is Bhanu Prakash
My branch is Electronics and communication Engineering'''
print(a)

b = """it does not matter wheather we 
enclose  our string  in 
single or double quotes, 
the output remains same """
print(b)

# *****Accessing character of string********
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) #Throw an error

# ******Looping through the string*******
print("using for loop: ")
for character in name:
    print(character)

for character in a:
    print(character)    