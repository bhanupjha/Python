#string are immutable
str1 = "Bhanu"
print(len(str1))

#*******upper() method**********
str1 = "AbcDEfghIJ"
print(str1.upper())

#*******lower() method*********
str1 = "AbcDEfghIJ"
print(str1.lower())

#********strip() method********
str2 = "  Silver Spoon  "
print(str2.strip())

#*********rstrip() method******
str3 = "Hello !!!"
print(str3.rstrip("!"))

#**********replace() method****
str2 = "Silver Spoon"
# print(str2.replace("Sp", "M"))
print(str2.replace("sp", "M"))

#***********split() method******
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".

#***********capatalize method******
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)

str2 = "hello WorlD"
print(str2.capitalize())

#***********center() method********
str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(60))
print(len(str1.center(60)))

# padding character
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))

#***********count() method**********
str2 = "Abracadabra"
print(str2.count("a"))

#**********endswith() method********
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 5, 10))

#***********find() method***********
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))

# The major difference being that index() raises an exception if value is absent
#************index() method**********
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Daniel")) #throw an error (if value is absent)

#***************isalnum() method*******
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "Welcome To, The Console"
print(str1.isalnum())

#****************isalpha() method******
str1 = "Welcome"
print(str1.isalpha())

str1 = "Welcome001"
print(str1.isalpha())

#**************islower() method*******
str1 = "hello world"
print(str1.islower())

#**************isprintable() method*****
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

str1 = "We wish you a\n Merry Christmas"
print(str1)
print(str1.isprintable())

#**************isspace() method********
str1 = "        "       #using Spacebar
print(str1.isspace())

str2 = "        "       #using Tab
print(str2.isspace())

#***************istitle() method*******
str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

#**************issuper() methhod*******
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

#***********startswith() method********
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

#************swapcase() method********
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

#*************title() method**********
str1 = "His name is Dan. Dan is an honest man."
print(str1.title())
