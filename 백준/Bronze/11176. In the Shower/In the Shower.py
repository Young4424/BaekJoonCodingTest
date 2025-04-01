import sys


T = int(sys.stdin.readline().strip())


for _ in range(T):
    E,N = map(int,sys.stdin.readline().split())
    count = 0

    for _ in range(N):
        test = int(sys.stdin.readline().strip())

        if test > E:
            count +=1


    print(count)

