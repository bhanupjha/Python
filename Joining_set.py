# ****************union()***************
# union() method prints all the items and return a new set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)

# ****************update()******************
# update() method print all items & add item into the existing set from another set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # before update
# print(cities, cities2)
# cities.update(cities2)
# # after update
# print(cities, cities2)

# ******************intersection()*****************
# intersection() method print only item that are similar to both the sets and return new set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)

# ***************intersection_update()***********
# intersection_update() method print similar item & update into the existing set from another  set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)

# **************symmetric_difference()**************
# symmetric_difference() method prints disimilar items to both the sets
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# *************symmetric_difference_update()***********
# symmetric_difference_update() method print disimilar items & update into the existing set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)

# **************difference()*******************
# difference() method print only items that are only present in the original set and not in the both set 
# difference() method return a new set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.difference(cities2)
# print(cities3)

# ***************difference_update()***************
# difference_update() method print only items that are only present in the original set and not in the both set 
# difference_update() method update into the existing set from another set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Madrid"}
# cities.difference_update(cities2)
# print(cities)