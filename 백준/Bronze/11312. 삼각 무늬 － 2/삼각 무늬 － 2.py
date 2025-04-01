import sys


T = int(sys.stdin.readline().strip())


for _ in range(T):
    A, B = map(int,sys.stdin.readline().split())

    recur_num = A//B

    if recur_num == 1:
        print(1)

    else:

        a = 1
        result = 0

        for _ in range(recur_num):
            result +=a
            a +=2

        print(result)
