#Mutable   = Internal state can be changed, memory address same. 
#               i.e. list, dict, sets
#Immutable = Internal state can't be changed, memory address diff, new object will be created to point
#               i.e. int, bool, string, float, tuple

#Mutable
dict1 = {"name": "Lallan", "age": 30}
print("dict1 is pointing to : ", id(dict1), "for value: ", dict1)

dict1["name"] = "Kumar"
dict1["age"] = 31
print("dict1 is pointing to : ", id(dict1), "for value: ", dict1)

#Immutable
str1 = "111111"
print("str1 is pointing to : ", id(str1), "for value: ", str1)

str1 = "abcde"
print("str1 is pointing to : ", id(str1), "for value: ", str1)
