l=[45,54,34,2,3,1,67,89,6,7,9,10]
print(l)
l.reverse()              # reverse():- reverse the index  element in the list
l.append(4)              # appened(element):- simply adding one more element
l.sort()                 # sort ():- sorting the list in ascending order
l.sort(reverse=True)     # sort (reverse=true):- sorting the list in descending order
print(l)
#print(l.count(2))       #l.count(element):- searching the no. of element present ,similar to the seacrh element in the list
#print(l.index(5))       #l.index(index no.):- simply print the element present in the index no.
m=l.copy()               # l.copy():- use to change the element of the list without changing the name of list(it's make a copy of the list)
m[0]=0
print(m)
n=[200,9000,999]
k=l+n                    #concatenate: (k=l+n) bass baju mai lage rakh diya h 
print(k)
l.extend(n)              #l.extend :- yeh bhi dsame kam karta h concatenate ki tarah
print(l)