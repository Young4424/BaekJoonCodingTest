# 첫째 줄에 입력으로 주어진 N개의 정수수
count = int(input())

# 두번째 줄의 정수의 모임임
numbers = map(int,input().split())

# 리스트 변환
num_list = list(numbers)

# 세번 째 줄의 정수 v
num = int(input())

# 개수 세기 위한 변수수
count = 0

for item in num_list:
    if num == item:
        count +=1

print(count)