import sys
from collections import deque

test_case = int(sys.stdin.readline().strip())


for _ in range(test_case):
    # N : 문서의 개수
    # M : 몇 번째로 인쇄되었는지 궁금한 문서가 현재 queue 에서 몇 번째 위치에 있는지 나타내는 정수

    N,M = map(int,sys.stdin.readline().split())

    num_list = list(map(int,sys.stdin.readline().split()))

    my_deque = deque([(index,importance) for index,importance in enumerate(num_list)])
    
    count = 0

    while my_deque:
        current_importance = my_deque.popleft()
        if any(current_importance[1] < item[1] for item in my_deque):
            my_deque.append(current_importance)
            

        else:
            count +=1
            if current_importance[0] == M:
                break

    print(count)
