import sys

N = int(input())

# 리스트의 sort 함수는 O(n logn)
# 입력데이터가 매우 큰 경우, 메모리 제한이 걸릴 수 있다.

# 카운팅 정렬 방식으로 활용하기 
num_count_list = [0]*10001


for number in range(0,N):
    enter = int(sys.stdin.readline())
    num_count_list[enter] +=1


for index, item in enumerate(num_count_list):
    if item !=0:
        for result in range(item):
            print(index)
    