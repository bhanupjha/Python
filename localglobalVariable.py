x = 4 # global variable

def my_fun():
    y = 3 # local variable
    print("The local variable is: ", y)
    # We can access the value of the global variable x from within the function.
    print("The global variable is: ", x)


my_fun()
print("The global variable is: ", x)
# we cannot access the value of the local variable y outside of the function.
# print("The local variable is: ", y) # this will cause an error because y is a local variable and is not accessible outside of the function


# ********************global keyword************************************
a = 5 # global variable

def my_fun():
    b = 3 # local variable
    # Note: we used the global keyword to declare that we want to modify the global variable x from within the function.
    # As a result, the value of a is changed to 10.
    global a
    a = 10 # this will change the value of the global variable x
    print("The local variable is: ", b)
    print("The global variable is: ", a)


my_fun()
print("The global variable is: ", a)