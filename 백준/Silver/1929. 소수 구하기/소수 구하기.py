
import sys

M,N = map(int,input().split())

# 에라토스테네스의 체 초기화 : N까지의 모든 수를 소수로 간주
is_prime = [True] * (N+1)
is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아니다.


# 에라토스테네스의 체 알고리즘
for i in range(2,int(N**0.5) +1):
    if is_prime[i]: # i가 소수인 경우
        # i의 배수들을 모두 소수가 아닌 것으로 표시
        # i*i로 시작하는 이유는 i2,i3,...,i(i-1)은 이미 이전 단계에서 처리되었기 때문이다.
        for j in range(i*i,N+1,i):
            is_prime[j] = False


# M부터 N까지 모든 소수 출력
for i in range(M,N+1):
    if is_prime[i]:
        print(i)
