# String are immutable
name = "!!!!Lallan !!!! Kumar!!!!!"
print(name.upper())
print(name.lower())
print(name.rstrip("!")) # Right strip
print(name.lstrip("!")) # Left strip
print(name.replace("Lallan", "Allen"))
print(name.replace("lallan", "kumar")) # Nothing found to replace
print(name.replace("Kumar", "Hardiman")) 
list1 = name.split(" ")
print(list1)

exampleStr1 = "my name is Lallan Kumar!" # first capatilize then others small
print(exampleStr1.capitalize())
print(exampleStr1.center(100)) # add spaces 
print(exampleStr1.count("a"))  # count number of character
print(exampleStr1.endswith("!")) # return true/false where string ends with given character
print(exampleStr1.endswith("Kumar!", 0, len(exampleStr1))) # return true/false where string ends with given character b/w subScript number
print(exampleStr1.startswith("my"))
print(exampleStr1.find("name")) # return subsScript of first occurance of given value
print(exampleStr1.find("Allen")) # return subsScript -1 if not found
#print(exampleStr1.index("Allen")) # return exception
print(exampleStr1.index("Lallan")) # return subsScript -1 if not found

alNumString = "123abc456DEF"
alPhaString = "abcdefgh"
nonPrintableStr = "I am good\n"
onlySpaceStr = "    "
titleStr = "My Name Is Lallan Kumar"
swapCaseStr = "mY nAME iS lALLAN"
print(alNumString.isalnum()) # to check alpha numeric string
print(alPhaString.isalpha()) # to check alpha string
print(alPhaString.islower())
print(alPhaString.isprintable())
print(nonPrintableStr.isprintable()) # return false as \n is not printable chars
print(onlySpaceStr.isspace()) # return true if only and only space is present
print(titleStr.istitle()) # return true if first letter of word is capital
print(swapCaseStr.swapcase()) 
print(swapCaseStr.title()) 



