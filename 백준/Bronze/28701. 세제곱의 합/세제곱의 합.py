import sys

n = int(sys.stdin.readline().strip())

sum = 0
sum_2 = 0
sum_3 = 0
for i in range(1,n+1):
    sum +=i
    sum_3 += i**3


print(sum)
print(sum**2)
print(sum_3)

