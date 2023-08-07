fruits = "Mango,banana"
len1 = len(fruits)
print(len1)
print("Mango,banana is a", len1, "letter word.")

print(fruits[0:5])  #including 0 but not 5

print(fruits[1:5])  #including 1 but not 5

print(fruits[:5])   #slicing from start

print(fruits[4])

print(fruits[6:])   #slicing till end

print(fruits[2:8])  #slicing in between

print(fruits[2:-3]) #slicing using negative index 
print(fruits[2:len(fruits)-3])
print(fruits[0:-6])
print(fruits[-7:-6])

print(fruits[-2:9]) # (-2/len(fruits -2) : 9 )10 to 9 is not possible , so it doesn't print anything



