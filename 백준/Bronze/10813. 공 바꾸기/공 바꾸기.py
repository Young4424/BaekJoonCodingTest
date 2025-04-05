import sys

n,m = map(int,sys.stdin.readline().split())

num_list = [i for i in range(1,n+1)]


def swap(a,b):
    number = a
    a = b
    b = number

    return a,b


for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())

    new_a, new_b = swap(num_list[i-1],num_list[j-1])

    num_list[i-1] = new_a
    num_list[j-1] = new_b


for item in num_list:
    print(item, end=' ')

    