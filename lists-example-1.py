#Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish i.e. mixed data data types
mylist = [] #declaration of Lists
mylist.append(100.30) #use append to fill Lists
mylist.append(99)
mylist.append(100)
mylist.append("ABC")

#use square brackets with index value to access the value
print(mylist[0]) # prints 100.30
print(mylist[1]) # prints 99
print(mylist[2]) # prints 100
print(mylist[3]) # prints ABC 

# printing using loop
for x in mylist:
    print(x)
	
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = even_numbers + odd_numbers # adding lists
print(all_numbers)
print(len(all_numbers)) # using len() to get nuber of items
print(all_numbers.count(5)) # using count() to check item's count

listOne = [1, 2, 3, "a", "b", 2, 3, "b"]
print(len(listOne))
print(set(listOne)) # using set() to remove duplicate items