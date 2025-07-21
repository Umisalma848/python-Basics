a=2000
b=3000
print(1) if a>b else print(0) if a==b else print(2) 

c=10 if (a<b) else ""   #syntex: result= value_if_true if condition else value_if_false
print(c)

# enumerate function(without)
marks=[12,13,23,34,45,56,67,78,89]
index =0
for mark in marks:
    print(mark)
    if(index==4):
        print("study")
    index+=1
# enumerate function(with)
marks=[12,13,23,34,45,56,67,78,89]

for index,mark in enumerate(marks):
    print(mark)
    if(index==4):
        print("study")
   
# satrating point given
for index,mark in enumerate(marks,start=2):
    print(mark)
    if(index==4):
        print("study")
   

