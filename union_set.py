s1={1,2,3,4,5}
s2={3,4,5,6,6,7}

# union and update
print(s1.union(s2)) 
s=s1.update(s2)
print(s1,s2)

# interaction and interaction update
s=s1.intersection(s2)
print(s)

# difference and difference_update
s=s1.difference(s2)
print(s)

print(s1.isdisjoint(s2))     #isdisjoint (): jo dono mai common nahi h
print(s1.issuperset(s2))     #issuperset (): jiske ander sare values aajaye
print(s1.issubset(s2))       #issubset (): s2 s1 ka subset h ki nhi 

s1.add(54)                   # add (): set ke ander koyi value put karna
print(s1)
s1.remove(5)                 # remove (): set ke ander koyi value hatana karna
s1.discard(3)
s1.pop()
s1.clear()
del s2()
print(s1)