# 백준 30802
import sys
import math

num = int(sys.stdin.readline())


S,M,L,XL,XXL,XXXL = map(int,sys.stdin.readline().split())

T,P = map(int,sys.stdin.readline().split())


# T셔츠 묶음의 총합을 저장할 변수수
k = 0

# 각 사이즈 별 티셔츠 개수를 리스트로 관리
num_T_shirt = [S,M,L,XL,XXL,XXXL]

# 각 사이즈별 필요한 묶음 수를 저장할 리스트트
a_list = []

# 각 사이즈별로 필요한 묶음 수 계산
for item in num_T_shirt:
    if item % T == 0: 
        k = item//T # 필요한 묶음 수 계산
        a_list.append(k)

    else:
        k = math.ceil(item/T) # 올림하여 필요한 묶음 수 계산 
        a_list.append(k)

# 총 필요한 티셔츠 묶음 수를 저장할 변수수
result = 0

for i in a_list:
    result = result + i

# 총 티셔츠 묶음 수 출력력
print(result)

# 필요한 펜 묶음 수와 남는 펜 개수 출력력
print(num//P,end= ' ') # 필요한 펜 묶음 수 (총 인원수를 한 묶음 당 펜 개수로 나눈 몫)
print(num%P) # 남는 펜 개수 (총 인원수를 한 묶음 당 펜 개수로 나눈 나머지)