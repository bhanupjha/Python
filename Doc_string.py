# def square (n):
# # it is not comment, it is docstring ..> used right after the definition/function/method/class    
#     '''Takes in a number n, returns the 
#      square of n'''
#     print(n**2)
# square(5)    


# we can access these doctring using the doc attribute
# def square (n):
#     '''Takes in a number n, returns the 
#      square of n'''
#     return n**2
# print(square.__doc__)


# def square (n):
#     print(n)
#     '''Takes in a number n, returns the 
#      square of n'''
#     return n**2
# # it doesn't print these line , because its n't a doctring..> it is write below the 
# # function name or above the function body
# print(square.__doc__) # in this case docstring is None
