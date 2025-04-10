import sys


A,P,C = map(int,sys.stdin.readline().split())

'''

div 1: 누구나 참여 가능, 수상 시 shake(C) 진출 가능
div 2 : 수상 해도 shake 진출 x



'''

if (A + C) > P:
    print(A + C)

else:
    print(P)

