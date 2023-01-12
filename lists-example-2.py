numbers = []
strings = []
names = ["John", "Eric", "Jessica"] # filling while declaration

# append to fill numbers list
numbers.append(1)
numbers.append(2)
numbers.append(3)

# append to fill strings list
strings.append("hello")
strings.append("world")

second_name = names[1] # use lists value to fill variable


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)