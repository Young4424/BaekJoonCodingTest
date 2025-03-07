import sys

N = int(input())

# 명부 입력받을 공간
assign_list = []


for i in range(N):
    # 나이와 이름을 받는다.
    age, name = map(str,input().split())

    # i의 경우, 가입한 순서를 기록하기 위해 넣는다.
    assign_list.append([int(age),i,name])


assign_list.sort()

for i in range(N):
    print(assign_list[i][0], assign_list[i][2])