# this is the regualr program to be used
# def double (x):
#     return x*2

# using a lambda function: anonymous function without name usedd in short program or in one liner 

double= lambda x:x*3
cube= lambda x:x**3
avg= lambda x,y,z:(x+y+z)/3

print(double(2))
print(cube(2))
print(avg(2,3,4))