import sys

N = int(sys.stdin.readline().strip())

# 1부터 n까지
for i in range(1,N+1):
    print(' ' * (N-i) + '*'*(2*i-1))

for j in range(N-1,0,-1):
    print(' '*(N-j) + '*'*(2*j-1))