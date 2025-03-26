import sys

N,M = map(int,sys.stdin.readline().split())

money = 100*N

if money>=M:
    print('Yes')

else:
    print('No')