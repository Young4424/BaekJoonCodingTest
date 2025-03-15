# 누적합에 관한 문제
"""
[0, 0, 0, 0],  # 0층: 0호, 1호, 2호, 3호
[0, 0, 0, 0],  # 1층: 0호, 1호, 2호, 3호
[0, 0, 0, 0]   # 2층: 0호, 1호, 2호, 3호

"""

import sys

N = int(sys.stdin.readline())

for _ in range(N):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    # 0층부터 k층까지, 1호부터 n호까지의 2차원 배열 생성 
    apartment = [[0]*(n+1) for _ in range(k+1)]


    # 0층에서 i호는 각각 i명산다.

    for i in range(1,n+1):
        apartment[0][i] = i


    # 자기 위치에서의 사람 명수

    for floor in range(1,k+1): # 0층의 경우는 했음
        for room in range(1,n+1): # 1호는 무조건 1
            apartment[floor][room] = apartment[floor][room-1] + apartment[floor-1][room]


    print(apartment[k][n])