import math
result = math.sqrt(4)
print(result)

#*************from keyword*****************
#importing specific function or variable
from math import sqrt
result = math.sqrt(9)
print(result)

#**************[* wildcard]******************
#importing everything
from math import *
result = math.sqrt(64)
print(result)
print(pi)

#**************as keyword********************
#rename module name
import math as m
result = m.sqrt(49)
print(result)

#**************dir function*******************
#list all the names defined in module
import math 
print(dir(math))
print(math.nan,type(nan))  # type of any function