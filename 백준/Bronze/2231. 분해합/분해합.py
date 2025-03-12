import sys

num = int(sys.stdin.readline().strip())

result = 0

digit = len(str(num))

# 1 ~ N-1에서 max(1,N-9*digit) ~ N-1로 줄일 수 있다.
min_range = max(1,num - 9*digit) 

for i in range(min_range,num):
    digit_sum = i + sum(map(int,str(i)))

    if digit_sum == num:
        result = i
        break


print(result)

