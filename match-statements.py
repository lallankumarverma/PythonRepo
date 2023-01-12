num = int(input("Enter num"))
print("Your num is: ", num)

match num:
    case 0:
        print("num is zero")
    case _ if (num < 0 ):
        print("num is negative")    
    case _ if (num > 0 ):
        print("num is positive")




