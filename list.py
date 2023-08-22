# list1 = [1,2,2,3,5,4,6]
# list2 = ["Red", "Green", "Blue"]
# print(list1)
# print(list2)

# details = ["Abhijeet", 18, "FYBScjg, 0.64"]
# print(details) # list can contain items of different data types.

# ***********List index***********************
# colors = ["Red", "Green", "Blue", "yellow", "Green"]
#          [0]     [1]      [2]      [3]      [4]
# print(colors[3])
# print(colors[1])
# print(colors[0])

#First method of Negative index:
# colors1 = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors1[-1])
# print(colors1[-3])
# print(colors1[-5])

#second method of negative index:
# marks = [3, 5, 6, "Hello", True, 6, 7 , 2, 32, 345, 23]
# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # change to Positive index

# *********Check  an item present inn the list or not?*************
# colors2 = ["Red", "Green","Yellow", "Blue", "Green"]
# if "Yellow" in colors2:
#     print("Yellow in present in the list")
# else:
#     print("Yellow is absent in the list")    

# colors3 = ["Red", "Green","Yellow", "Blue", "Green"]
# if "Orange" in colors3:
#     print("Orange in present in the list")
# else:
#     print("Orange is absent in the list")

# **********Range of Index**********************
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes
# print(animals[len(animals)-7:len(animals)-2])	#change to positive index

# animals1 = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals1[4:])	#using positive indexes
# print(animals1[-4:])	#using negative indexes
# print(animals1[len(animals1)-4:])

# animals2 = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals2[:6])	#using positive indexes
# print(animals2[:-3])	#using negative indexes
# print(animals2[:len(animals2)-3])	

# animals3 = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals3[::2])		#using positive indexes
# print(animals3[-8:-1:2])	#using negative indexes
# print(animals3[len(animals3)-8:len(animals3)-1:2])	

# animals4 = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals4[1:8:3])

