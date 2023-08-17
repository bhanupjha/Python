# *******Default Argument**************
# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy")
# name("Bhanu", "Deepu", "Osho")
# name("Bhanu", "Deepu")

# def average(a=9, b=1):
#     print("The average is: ", (a+b)/2)

# average()
# average(1,5)
# average(1)
# average(b=9)

# ***********Keyword Argument*****************
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name(mname = "Peter", lname = "Wesker", fname = "Jade")

# def average(a=9, b=1):
#     print("The average is: ", (a+b)/2)

# average(b=9, a=5)

# ****************Required Argument*****************
# Example 1: when number of arguments passed does
#  not match to the actual function definition

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")   #TypeError: name() missing 1 required positional argument: 'lname'


# Example 2: when number of arguments passed matches 
#     to the actual function definition.

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Ego", "Quill")

# def average(a,b,c=1):
#     print("The average is: ", (a+b+c)/2)

# average(8,9)

# ************Variable-length arguments*********
# def name(*name):
#     print("Hello,", name[0], name[1], name[2])

# name("James", "Buchanan", "Barnes")

def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    print(i)
    sum = sum + i
  print("Average is: ", sum / len(numbers))
  # return 7
  # return sum / len(numbers)


average(4, 6)
# average(b=9)

# c = average(5, 6, 7, 1)
# print(c)


# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")
