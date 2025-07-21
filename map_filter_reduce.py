# def double (x):
#     return x**3
from functools import reduce
cube= lambda x:x**3
print(cube(2))

""" MAP: here we can print the list by cubic of all the elements present in the list by using map and  also
 can be changed as a tuple set"""

l=[1,2,3,4,5]
print(list(map(cube,l)))
print(list(filter(lambda x:x>3,l)))   # FILTER:help to filter or searching the element in a list
print(reduce(lambda x,y:x+y,l))       # REDUCE : help to reduce the values inside in a list and it has to be imported