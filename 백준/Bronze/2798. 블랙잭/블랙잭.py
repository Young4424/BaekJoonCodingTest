import sys

N,M = map(int,sys.stdin.readline().split())


num_list = list(map(int,sys.stdin.readline().split()))

max_result = 0

for i in range(0,N):
    for j in range(0,N):
        for k in range(0,N):
            if i != j and j != k and k != i:
                if (num_list[i] + num_list[j] + num_list[k]) <= M:
                    if max_result < num_list[i] + num_list[j] + num_list[k]:
                        max_result = num_list[i] + num_list[j] + num_list[k]


print(max_result)
                    