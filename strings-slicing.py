# String Slicing []
fruit = "Mango"
len1 = len(fruit) # len() to get length of string
print(len1)
print(fruit[0:5]) # include 0 but not 5
print(fruit[1:5]) # include 1 but not 5
print(fruit[:5])  # automatically add 0 in first place
print(fruit[:])   # automatically add 0 in first place, length in second

# Negative Slicing - Python add length of string automatically
print(fruit[:-3])
"""
How [0:<length of fruit> - 3]
    [0:5-3]
    [0:2]
Resultant: Ma        
"""
print(fruit[-1:-3])
"""
How [<length of fruit> - 1:<length of fruit> - 3]
    [5-1: 5-3]
    [4:2]
Resultant: <Nothing> No Sense        
"""
print(fruit[-3:-1])
"""
How [<length of fruit> - 3:<length of fruit> - 1]
    [5-3: 5-1]
    [2:4]
Resultant: ng
"""

print(fruit[-4:-2]) # print an
