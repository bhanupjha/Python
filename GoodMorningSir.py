import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
minute = int(time.strftime('%M'))
print(minute)
second = int(time.strftime('%S'))
print(second)
# https://docs.python.org/3/library/time.html#time.strftime

if(hour > 5 and hour < 12):
    print("Good Morning")
elif(hour > 12 and hour < 17):
    print("Good afternoon")
elif(hour > 17 and hour < 20):
    print("Good evening")
else:
    print("Good night")            