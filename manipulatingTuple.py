# ** tuples are immputable, If we want to change tuple items, then we must convert 
#   the  tuple to a list, perform operation on that list, convert back into tuple **

# countries = ("spain", "Italy", "India", "England", "Germany")
# #   #          [0]      [1]       [2]      [3]        [4]
# temp = list(countries) # convert into list
# print(countries) # its print tuple
# print(temp) # its print list
# temp.append("Russia")  # add item
# temp.pop(3)            # remove item
# temp[4] = "Finland"    # change item
# countries = tuple(temp)  # convert back into tuple
# print(countries)

#*********concatenate two tuples without converting into list**************
# countries = ("Pakistan", "Afghanistan", "Bangladesh", "shrilanka")
# countries2 = ("Vietnam", "India", "China")
# SouthEastAsia = countries + countries2
# print(SouthEastAsia)

#**********count() method********************
# tuple1 = (0,1,2,3,2,3,1,3,2)
# res = tuple1.count(3)
# print("count of 3 in tuple1 is: ", res)

#**********index() method******************
tuple1 = (0,1,2,3,2,3,1,3,2)
res = tuple1.index(2)  # if the element is not present, raises value error
print("First occurence of 2 is: ", res) 