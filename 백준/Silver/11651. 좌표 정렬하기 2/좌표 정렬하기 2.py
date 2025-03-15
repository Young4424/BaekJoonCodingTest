import sys
N = int(sys.stdin.readline())

num_list = []

for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    num_list.append((b,a))


num_list.sort()

for item in num_list:
    print(item[1],item[0])

    