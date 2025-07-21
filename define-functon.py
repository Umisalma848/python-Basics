# def funtion : seficify the calculation according to our need it is user define function
# built in funtion: set(),tupel(),list(),max(),min(),len(),sum(),dic(),

def gmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isgreater(a,b):
    if(a>b):
        print("first greater number")
    else:
        print("second greater number")  
def islesser(a,b):
    pass   # mai wapis aungi tab tak aage ke program execute karo

a= int(input("enter the number for a:",))              
b= int(input("enter the number for b:",)) 
gmean(a,b)
isgreater(a,b)

c= int(input("enter the number for c:",))              
d= int(input("enter the number for d:",))
gmean(c,d)
isgreater(c,d)