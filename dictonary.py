# the dictionary is a  unordered collection of data containing a key:value pairs
dict={"name":"umi",
      "marks":899, 
      "total":"subject"}
print(dict)
print(dict.keys())    # keys used to print only key
print(dict.values())  # values are used to print the value of respected key
print(dict.items())   # items used to print the key value paired

for key in dict.keys():
    print (f"the value correspond to the key {key} is {dict[key]}")
    
for key in dict.keys():
    print ("the value correspond to the key {key} is {dict[key]}")