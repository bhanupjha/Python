# https://docs.python.org/3/library/time.html#time.strftime
import time
timestamp = time.strftime('%H:%M:%S') # strftime is function which is gives hour and minute
# The return value of strftime() is a string
name = input("Enter you name:  ")
hour = int(time.strftime("%H"))
# hour = int(input("Enter hour: "))
# print(hour)
if(hour >= 5 and hour < 12):
    print("Good Morning", name)
elif(hour >= 12 and hour < 17):
    print("Good Afternoon", name)
elif(hour >= 17 and hour <= 20):
    print("Good Evening", name)
else:
    print("Good Night", name)            