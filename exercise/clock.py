import time
timeup=input(time.strftime('%H:%M:%S'))
print("the timestamp", timeup)
timeup1=int(time.strftime('%H'))
print("hours:",timeup1)
timeup2=int(time.strftime('%M'))
print("minutes:",timeup2)
timeup3=int(time.strftime('%S'))
print("secondes:",timeup3)

# Hours=int(time.strftime('%H'))
# minuts=int(time.strftime('%M'))
# seconds=int(time.strftime('%S'))

if(timeup1>5 and timeup1<12 and timeup2 >00 and timeup3>00):
    print("good morning sir")
elif(timeup1>12 and timeup1<16  and timeup2 >00 and timeup3>00):
    print("good afternoon sir")   
elif(timeup1>16 and timeup1<19  and timeup2 >00 and timeup3>00):
    print("good evening sir")     
else: 
    print("good night sir") 