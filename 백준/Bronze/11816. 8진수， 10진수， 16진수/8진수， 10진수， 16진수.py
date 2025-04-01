import sys

T = (sys.stdin.readline().strip())

if T[0] =='0':
    if T[1] =='x':
        T = int(T,16)
        print(T)

    else:
        T = int(T,8)
        print(T)

else:
    T = int(T)
    print(T)