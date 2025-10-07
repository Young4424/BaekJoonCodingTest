import sys

# 각 종류의 주문서들의 개수 N, M

N,M = map(int, sys.stdin.readline().split())


a_i = list(map(int,sys.stdin.readline().split()))

b_i = list(map(int,sys.stdin.readline().split()))

luck_sum = 0 

for i in range(N):
    luck_sum += a_i[i]


for j in range(M):
    if b_i[j] != 0:
        luck_sum *= b_i[j]


print(luck_sum)

    

 