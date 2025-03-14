import sys

N = int(sys.stdin.readline())

A_list = set(map(int,sys.stdin.readline().split())) # 리스트 대신 집합 사용

M = int(sys.stdin.readline())

M_list = list(map(int,sys.stdin.readline().split()))


for item in M_list:
    if item in A_list:
        print(1)

    else:
        print(0)