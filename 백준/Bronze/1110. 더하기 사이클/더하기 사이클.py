import sys

n = int(sys.stdin.readline())

num = n
cycle = 0

while True:
    a,b = divmod(num,10) # 몫, 나머지
    num = (b*10) + ((a+b)%10)
    cycle+=1

    if num == n:
        break

print(cycle)