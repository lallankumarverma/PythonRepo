str1 = "Lallan"
str2 = """I am good boy   
123456
Testing

'I will leanr anything'
Who says
It's his task
"""
#Triple double/single qaotes allows multilines string manipulation
print(str1)
print(str2)
print("\n")
print(str1[0]) # String is like array of characters
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[5])
# print(str1[6]) This will throws error index out of bound

for character in str2: # for loop to travers each characters
    print(character)

