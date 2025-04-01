import sys


T = int(sys.stdin.readline().strip())


for _ in range(T):
    cookie, ate = map(int,sys.stdin.readline().split())

    if cookie % ate == 0:
        today_ate = cookie//ate

    else:

        today_ate = (cookie//ate) + 1

    print(today_ate)



    