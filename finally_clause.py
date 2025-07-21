def func():
    try:
        a=input("enter the input here:")
        for i in range(1,11):
           print(f"the multiplication of {int(a)}x{i}={int(a)*i}") 
    except:
        print("error occurred")        

    finally:
        print(" i am always excuted")

x=func()
print(x)        

def func1():
  
    try:
        l=[1,2,3,4]
        i=int(input("enter the index here:"))
        print(l[i])
        return 0
    except:
        print("error occurred")        
        return 1
    finally:
        print(" i am always excuted")

y=func1()
print(y)        