# string format can be done by python using the format method
# txt = "for only {price: .2f} dollars!"
# print(txt.format(price = 49))

# ************old approach***************
# letter = 'Hey my name is {} and i am from {}'
# country = "India"
# name = "Bhanu"
# print(letter.format(name,country))
# # when we write like this:-
# # print(letter.format(country,name))
# # we could n't expected output

# to fix this we write code like:-
# letter = 'Hey my name is {1} and i am from {0}'
# country = "India"
# name = "Bhanu"
# print(letter.format(country,name))

# *************using f-string**************
# country = "India"
# name = "Bhanu"
# print(f"Hey my name is {name} and i am from {country}") # populate the name and country
# # when we don't want to populate then we use double middle bracket to print as we given f-string
# print(f"we us f-string like this: Hey my name is {{name}} and i am from {{country}}") 

# price = 39.8600
# txt = f"for only {price: .2f} dollars!"
# print(txt)
# # print(f"for only {price: .2f} dollars!")

# val = 'Geeks'
# print(f"{val} for {val} is a portal of {val}")

# name = 'Tushar'
# age = 23
# print(f"hello, my name is {name} and i'm {age} years old")

# we can use single statement as well
# print(f"{2 * 30}")