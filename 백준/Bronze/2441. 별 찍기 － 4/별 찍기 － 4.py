import sys

n = int(sys.stdin.readline().strip())

empty = 0

for i in reversed(range(n+1)):
    print(' '* empty,end="")
    print('*'*i)
    empty +=1
