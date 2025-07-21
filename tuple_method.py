tup=(1,2,3,4,5,6,7,8)
temp=list(tup)
print("the list is",temp)
print("the tuple is",tup)

# manuipulating by change the tuple into the list than it can be changed otherwise ot change
temp[0]="umi"            #change item
temp.append(1000)        #add item
temp.pop(4)              #remove item :-it remove the element present in that index
tup=tuple(temp)
print(tup)

tup1=(100,2000,300,4000)
newtup =tup + tup1          #tuple mai concatinate kar sakte h
print(newtup) 

rus=tup.count(4)            #count :- use to coount the no. of search element present in the tuple
print("the element count is ",rus)

rus1=tup1.index(100)        #index(index no.):- simply print the element present in the index no.   [index(element,start,end)] 
print("the element index is ",rus1)

tup2=len(temp)  
print(tup2)