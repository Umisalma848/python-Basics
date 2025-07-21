for i in range(5):               #square pattern
    for j in range(5):
        print('*',end='')
    print ('')  

print()

for i in range(0,5):               #side pyramid pattern
    for j in range(0,i+1):
        print('*',end='')
    print ('')       

print()

for i in range(0,5):                # inverted side pyramid pattern
    for j in range(0,5-i):
        print('*',end='')
    print ('')       

print()

for i in range(1,5+1):              # pyramid pattern
    for j in range(0,5-i):
     print(" " , end='') 
    for k in range (1,2*i):
     print('*',end='')
      
    print ('')       

print()

for i in range(5,0,-1):              # inverted pyramid pattern
    for j in range(5-i):
       print(' ',end='')
    for j in range (2*i-1):
       print("*" , end='') 
      
    print ('')       

print()

 # butterfly pattern

for i in range(0,5+1):               
    for j in range(0,i):
        print('*',end='')        
    for j in range(2*(5-i)):  
        print(" ", end="")             
    for j in range(i):
        print('*',end='')
    print ('')       

for i in range(5,0,-1):               
    for j in range(0,i):
        print('*',end='')        
    for j in range(2*(5-i)):  
        print(" ", end="")             
    for j in range(i):
        print('*',end='')
    print ('')   
