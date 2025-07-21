# list is changeable
list= ["red","yellow","orange","pink"]   #[3,4,5,6] represent no. like this
print(list)
print(type(list))# datatype of the list
print(list[0])   #list indexing (positive)
list1= ["red",True,3,4,5,6,7,8]  #it can contain a different datatype
print(list1)
print(list1[-2])    #negative indexing :-(list[len(list1)-2])"works like this"

if 5 in list1:
    print("yes")
else:
    print("no")    
# same thing applicable to string
if "ed" in "orange":
    print("yes")
else:
    print("no")
# jump indexing (slicing)  
print(list1[0:5:3])
# list comprehension
list2=[i for i in range(10)]
print(list2)
list2=[i*i for i in range(10)]
print(list2)
list2=[i*i for i in range(10) if i%2==0]
print(list2)
