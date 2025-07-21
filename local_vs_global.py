x=10 #global variable

def function():
    global x  # change the outer value of x w hich is a global variable value
    x=5
    y=5  #local variable
    print(y)

function() 
print(x)
#print(y) #error occur due to the y is a local variable