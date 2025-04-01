import sys


T = int(sys.stdin.readline().strip())


for _ in range(T):
    try:
        a = int(sys.stdin.readline().strip())
        
        if a < 0:
            print('invalid input')

        else:
            print(a)


    except:
        print('invalid input')

    