dict1={"name":"umi","marks":899, "total":"subject"}
dict2={"id":70,"perfomance":89}

#update():it help to update or combining two dict in one dictionary
dict1.update(dict2)
print(dict1)

# clear(): clear or remove the dictionary conataining key:values pair and make a dictionary empty
dict1.clear()
print(dict1)

# pop(): used to pop or delete the one or two keys :values pair element in dictionary
# dict1.pop("name")
# print(dict1)

# popitem(): used to pop or delete the last keys :values pair element in dictionary
dict1.popitem()
print(dict1)


# del: used to delete the keys :values pair element in dictionary or the whole dictionary
del dict1
# print(dict2)