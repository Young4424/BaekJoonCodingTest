import sys


# 몫, 나머지 구하는 나머지 정리(고1때 배움움)

N,M,K = map(int,sys.stdin.readline().split())


print(K//M,end=' ')
print(K%M)
            