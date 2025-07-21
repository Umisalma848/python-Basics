# default arguement
def average(a=9,b=7):
   print("average of number is:",(a+b)/2) 
average()

# keyword arguement : do not sterr about the order of arguement
average(b=4,a=3)

# required argueement : the key value of arguement muust be enter
def average(a,b ,c=7):
   print("average of number by using requried is:",(a+b+c)/2) 
average(4,5)

# variable length arguement
def average(*number):
    sum=0
    for i in number:
        sum+=i
    print("average of number by using len:",sum/len(number)) 
average(4,5)

# return statement
def average(*number):
    sum=0
    for i in number:
        sum+=i
    return sum/len(number)
num=average(4,5,3,2,1)
print("return statement:",num)