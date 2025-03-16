import sys
import math

A,B,V = map(int,sys.stdin.readline().split())

'''

(A-B) * (n-1) + A > V

n-1일까지는 (A-B)까지 움직이다가, n일에는 A만큼 이동하면 V를 넘어설 수 있음
이때, 일 수는 정수이므로 올림 처리 해줘야함.


'''

n = math.ceil((V-B)/(A-B))
print(n)


