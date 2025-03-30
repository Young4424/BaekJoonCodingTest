import sys

hour,origin_minute = map(int,sys.stdin.readline().split())

cook = int(sys.stdin.readline())

if cook + origin_minute >=60:
    minute = int(cook+origin_minute) % 60
    hour += (cook+origin_minute)//60

    if hour >=24:
        hour = hour-24

else:
    minute = cook + origin_minute



print(hour,end=' ')
print(minute)


