# if-else statement

a=int(input("enter your age: "))
print("the age is", a)
if(a>18):
    print("you can drive the car")
else: 
    print("you can not drive the car")
print("woooo")

# elif statement

number=int(input("enter the number here: "))

if(number>0):
    print("the number is positive")
elif(number==0):
    print("the number is zero")   
elif(number==999):
    print("you are the special")     
else: 
    print("the number is negative")
print("woooo")

# nested if statement

marks=int(input("enter the marks here: "))

if( marks<33):
    print("the  student is fail with F grade")
elif(marks>33 and marks<50):
    print("the student grade is E")   
    if(marks>50 and marks<60):
        print("the student grade is D")  
    elif(marks>60 and marks<90):
        print("the student pass with the good marks")
    else:
        print("the student are the toppers and marks are above 90")    
else: 
    print("the marks is  in negative")
print("if fail try hard")    
print("if pass congratulation")