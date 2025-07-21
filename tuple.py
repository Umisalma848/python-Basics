#  the tuple is similiar to list but only change is "()" and "unchangeable"

tup=(1,2,3,4,5,6,7,8)
#tup[0]= 23          # the tuple can not changed any how
print(type(tup),tup)
tup1= ["red",True,3,4,5,6,7,8] 
print(tup1[-2])
print(tup1[0]) 
if 5 in tup1:
    print("yes")
else:
    print("no") 
print(tup1[0:5:3])