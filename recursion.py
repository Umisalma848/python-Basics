# factorial of a number
def factorial(n):
 if(n==0 or n==1 ):
    return 1
 else:
    return (n*factorial(n-1))
x=int (input("enter the number:"))       
print("factorial of number is:",factorial(x))    

# fibonacci sequence
def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
# xyz=int (input("enter the number:"))  
number = int (input("enter the number:"))     
print("fibonacci of number is:",fibonacci(number))    