# tuple1 = (1,2,2,3,5,4,6)
# print(tuple1)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple2)

# details = ("Abhijeet", 18, "FYBSCIT", 9.8)
# print(details)

# tup = (1)
# print(type(tup)) # The type of tup is integer
# tup = (1,)       # if we want to type of tup act as an tuple
# print(type(tup)) # then we add comma after digit/element

# # tup[0] = 34 # tuple are unchangeable

# *************positive indexing *****************
# country = ("Spain", "Italy", "India")
#  #           [0]      [1]      [2]
# print(country[0])
# print(country[1])
# print(country[2])
# # print(country[3]) # tuple index out of range

# *************Negative indexing *****************
# country = ("Spain", "Italy", "India", "England", "Germany")
#  #           [0]      [1]      [2]       [3]        [4]
# print(len(country)) 
# print(country[-1])
# print(country[-3])
# print(country[-4])

# ************check for item**********************
# country = ("Spain", "Italy", "India", "England", "Germany")
# if "Germany" in country:
#     print("Germany is present")
# else:
#     print("Germany is absent") 

# country1 = ("Spain", "Italy", "India", "England", "Germany")    
# if "Russia" in country1:
#     print("Russia is present")
# else:
#     print("Russia is absent")           

# ********Range of index************************
# animals = ("cat", "dog", "Bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# #  #         [0]    [1]    [2]     [3]     [4]     [5]     [6]       [7]     [8]
# print(len(animals))
# print(animals[3:7])  # using positive index
# # ** The element of end index provided will not be included **
# print(animals[-7:-2]) # using negative index
# print(animals[len(animals)-7:len(animals)-2]) # convert negative index to positive

# animals1 = ("cat", "dog", "Bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# #  #         [0]    [1]    [2]     [3]     [4]     [5]     [6]       [7]     [8]
# print(len(animals1))
# # # ** when no index provided , the interpreter print all the values till end **
# print(animals1[4:]) # using positive indexes
# print(animals1[-4:]) # using Negative indexes

# # # ** when no start index provided, the interpreter print all the value from start up to end index **
# print(animals1[:6])
# print(animals1[:-3])

# # # ** when no start and end index, all values will  be considered **
# print(animals1[:])
# print(animals1[::2]) # jump index = 2, alternate value will be printed
# print(animals1[-8:-1:2])
# print(animals1[len(animals1)-8:len(animals1)-1:2]) # convert negative index to positive

# print(animals1[1:8:3])  # jump index = 3, printing every third consecutive witin given range