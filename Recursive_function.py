# *********Factoroial of aany number********
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)

# def factorial(num):
#     if (num==0 or num==1):
#         return 1
#     else:
#         return (num * factorial(num-1))

# Driver code
# num = 7
# print("Number: ", num)
# print("Factorial: ", factorial(num))


# how it works??
# print(factorial(7))
# 7 * factorial(6)
# 7 * 6 * factorial(5)
# 7 * 6 * 5 * factorial(4)
# 7 * 6 * 5 * 4 * factorial(3)
# 7 * 6 * 5 * 4 * 3 * factorial(2)
# 7 * 6 * 5 * 4 * 3 * 2 * factorial(1)
# 7 * 6 * 5 * 4 * 3 * 2 * 1

# *************Fibonacci sequence**************
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8

# def fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))
    
# for steps of fibonacci series go through notes

# print(fibonacci(6)) # 6th no. element in fibonacci sequence i.e 8, when starting from 0
