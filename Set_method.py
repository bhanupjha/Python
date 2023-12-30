# several in-built method used for manupulating of set

# *********isdisjoint()***************
# check if items of given set are present in another set
# return false if item present else true
# disjoint sets..> no element common
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "seoul", "kabul", "Madrid"}
# print(cities.isdisjoint(cities2))


# *************issuperset()*************
# check if all the items of a particular set are present in original set
# return true if all the items are present else it return false
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Delhi"}
# print(cities.issuperset(cities2)) # all element of cities2 is present in cities i.e True
# cities3 = {"seoul", "kabul"}
# print(cities.issuperset(cities3)) # all element of  cities3 is not present in cities i.e False
# cities4 = {"seoul", "Madrid", "kabul"}
# print(cities.issuperset(cities4))


# **************isubset()******************
# check if all the items of the original set are present in particular set
# return true if all the item present else false
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities)) # all element of cities2 present in cities i.e True


# ***********add()**************************
# used to add a single item
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)


# **************update()********************
# add more than one item, create another set/list/tuple/dict and use update() method to add it
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "warsaw", "seoul"}
# cities.update(cities2)
# print(cities)


# **************remove()/discard()***************
# remove() & discard() method used to remove item in the list
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo")
# print(cities)


# Note: if we try to delete an item which is not present in set, then 
# remove() raises error whereas discard() does not
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("seoul") # seoul is not present in set so it raises an error i.e KeyError: 'seoul'
# print(cities)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # discard() does not raises any error, if element was not present in set, it prints as set given
# cities.discard("seoul") 
# print(cities)


# ****************pop()*****************
# it removes the last item of the set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.pop() # catch is that we don't know which items get popped as set  unordered
# print(cities)

# we can access the popped if we assign the pop()method to a variable
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop() 
# print(cities)
# print(item)


# *****************del**********************
# del is not method, it is a keyword which deletes the is set entirely
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# # we got an error, our entire set has been deleted there is no variable called cities which contain a set
# print(cities) 


# if we don't want to delete the entire set, then use clear() method
# ******************clear()**********************************
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities) # we get set() as a o/p because empty set represent as that


# ***************check if item exists*************
info = {"carla", 19, False, 5.9}
if "carla" in info:
    print("carla is present")
else:
    print("carla is absent")    