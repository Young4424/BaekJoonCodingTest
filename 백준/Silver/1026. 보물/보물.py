import sys

n = int(sys.stdin.readline())


list_A = list(map(int,sys.stdin.readline().split()))
list_B = list(map(int,sys.stdin.readline().split()))


list_A.sort()
list_B.sort(reverse=True)


result = 0

for i in range(len(list_A)):
    for j in range(len(list_B)):
        if i == j:

            result += list_A[i] * list_B[j]

print(result)