import sys


T = int(sys.stdin.readline().strip())

num_list = []

for _ in range(T):
    d,n,s,p = map(int,sys.stdin.readline().split())

    n_s = n*s # 실행횟수 * 실행 시간
    n_p = n*p + d # 실행 횟수 * 실행시간 + 병렬 개발 시간

    if n_s > n_p:
        print('parallelize')

    elif n_s == n_p:
        print('does not matter')

    else:
        print('do not parallelize')
    
    