hour, min = map(int,input().split())


if (min - 45) <0: # 분침의 숫자가 45보다 작아서 다시 60진수로 넘어가는 경우

    if hour - 1 <0: # 시간의 숫자가 0보다 작아서, 23시로 되돌아가는 경우
        hour = hour - 1 + 24
        min = 60 + (min - 45)


    else:
        hour -=1
        min = 60 + (min - 45)


else: # 아닌 경우
    min -= 45

print(hour,min)

