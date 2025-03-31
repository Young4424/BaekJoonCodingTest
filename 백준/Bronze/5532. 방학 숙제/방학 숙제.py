import sys
import math

list_num = []

for _ in range(5):
    number = int(sys.stdin.readline())
    list_num.append(number)


L = list_num[0]
A = list_num[1]
B = list_num[2]
C = list_num[3]
D = list_num[4]

if (A%C) == 0:
    kor = A//C

else:
    kor = A//C + 1

if (B%D) == 0:
    math = B//D

else:
    math = B//D + 1


if kor > math:
    print(L-kor)

else:
    print(L-math)



