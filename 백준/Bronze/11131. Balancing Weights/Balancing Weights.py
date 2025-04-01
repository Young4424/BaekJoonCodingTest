import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())

    num_list = list(map(int,sys.stdin.readline().split()))

    result = sum(num_list)

    if result > 0:
        print('Right')

    elif result < 0 :
        print('Left')

    else:
        print('Equilibrium')
