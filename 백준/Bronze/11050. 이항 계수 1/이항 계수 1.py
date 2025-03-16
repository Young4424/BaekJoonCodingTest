import sys


N,K= map(int,sys.stdin.readline().split())

"""


ex) (10)
    (2)  = 10*9 / 2!


"""



result = 1

for _ in range(K):
    result= result * N
    N = N-1

result2 = 1

for i in range(1,K+1):
    result2 *= i 



print(int(result/result2))
    
