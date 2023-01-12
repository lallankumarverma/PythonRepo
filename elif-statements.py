num = int(input("Enter num"))
print("Your num is: ", num)

if (num == 0):
    print("num is zero")
elif (num < 0):
    print("num is negative")
else:
    if (num > 0 and num <= 10):
        print("num is between 0 to 10")
    elif (num > 10 and num <= 20):
        print("num is between 10 to 20")
    else:
        print("num is greater than 20")
    print("num is positive")
