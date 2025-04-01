import sys
import copy

N,M = map(int,sys.stdin.readline().split())

num_list = []

for i in range(1,N+1):
    num_list.append(i)


for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())

    new_list = num_list[a-1:b]
    
    num_list[a-1:b] = new_list[::-1]
    

for item in num_list:
    print(item,end=" ")

    
    