import sys


a,b,c, = map(int,sys.stdin.readline().split())

result1 = int(a * b / c)
result2 = int(a/b*c)


if result1 > result2:
    print(result1)

else:
    print(result2)