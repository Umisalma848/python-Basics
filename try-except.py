a=input("enter the input here:")
for i in range(1,11):
 print(f"the multiplication of {int(a)}x{i}={int(a)*i}")   

# this above line show error when ever we enter the string or character and the below line cannot be executed(program is in hault)
 print("show the input answer here")
 print("end of the program")

# by usinng try except we can run the all program in one go and neglecting the  error
b=input("enter the input here:")
try:
 for i in range(1,11):
  print(f"the multiplication of {int(b)}x{i}={int(b)*i}")   
except:
 print("INVALID")  