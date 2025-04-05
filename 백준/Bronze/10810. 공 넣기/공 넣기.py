import sys

n,m = map(int,sys.stdin.readline().split())

num_list = [0] * n

for _ in range(m):
    i,j,k = map(int,sys.stdin.readline().split())
    
    for idx in range(i-1,j):
        num_list[idx] = k


for item in num_list:
    print(item, end=' ')
