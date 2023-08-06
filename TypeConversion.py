# **********Explicit Type Conversion****************

string = "10" #throws an error if the string is not a valid integer
number = 5
print("The sum of two number is: ", int(string) + number)


# ************Implicit Type Conversion*****************

# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))


