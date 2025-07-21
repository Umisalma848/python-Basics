# beak: its mean remove all the iteration after running to the loop
for i in range(15):
    print("5x",i+1,"=",5*(i+1))
    if(i==4):
     break
print("loop chod diya")    

# continues : its skip the iteration object and jump to the next iteration
for i in range(8):
 if(i==4):
    print("iteration chod diya")    
    continue
 print("5x",i,"=",5*(i))   

# do-while loop : it is a seet of instruction will execute atleast ones(exit controlled loop)   
#  emulate do-while loop: infinite while loop use with the break statement and than wrapped with the if statement to check the condition

while True:
   i=int(input("enter the number:",))
   print(i)
   i=i+1  
   if(i<=0): #if not i>0:
    break
