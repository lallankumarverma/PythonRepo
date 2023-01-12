import time
timestamp = time.strftime("%H:%M:%S") # to get time in H:M:S format
print(timestamp)
print(time.strftime("%H"))
print(time.strftime("%M"))
print(time.strftime("%S"))
print(time.timezone)

hoursStamp = int(time.strftime("%H"))

if(hoursStamp<12):
    print("Good Morning")
elif(hoursStamp>=12 and hoursStamp<=16):
    print("Good Evening")
else:
    print("Good Night")



