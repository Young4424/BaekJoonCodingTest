import sys

n,space = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))


for i in num_list:
    print(i-n*space,end= " ")