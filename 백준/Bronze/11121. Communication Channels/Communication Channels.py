import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    a,b = map(str,sys.stdin.readline().split())

    if a == b :
        print("OK")

    else:
        print("ERROR")
    