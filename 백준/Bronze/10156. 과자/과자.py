import sys

"""
과자 한 개의 가격 K
사려고 하는 과자의 개수 N
현재 가진 돈 : M

부모님에게 받아야 할 모자란 돈 계산


"""


K,N,M = map(int,sys.stdin.readline().split())

money_needed = (K * N) - M

if money_needed <= 0:
    money_needed = 0

print(money_needed)