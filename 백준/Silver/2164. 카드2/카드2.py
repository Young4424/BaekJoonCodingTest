import sys
from collections import deque

n = int(sys.stdin.readline().strip())

num_list = [i for i in range(1,n+1)]

my_deque = deque() # 빈 deque 사용
my_deque = deque(num_list)


# 원소 제거하기

while len(my_deque) != 1:
    popped_left = my_deque.popleft()
    my_deque.rotate(-1)

    
print(my_deque[0])
