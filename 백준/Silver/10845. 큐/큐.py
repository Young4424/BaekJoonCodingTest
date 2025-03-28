import sys

n = int(sys.stdin.readline())

num_list = []

for _ in range(n):
    order_list = []
    order_list = list(map(str,sys.stdin.readline().split()))

    if order_list[0] == 'push':
        num_list.append(int(order_list[1]))

    elif order_list[0] == 'size':
        print(len(num_list))

    elif order_list[0] == 'empty':
        if len(num_list) == 0:
            print(1)

        else:
            print(0)

    elif order_list[0] == 'pop':
        if len(num_list) == 0:
            print(-1)

        else:
            a = num_list.pop(0)
            print(a)
    
    elif order_list[0] == 'front':
        if len(num_list) == 0:
            print(-1)

        else:
            print(num_list[0])


    elif order_list[0] == 'back':
        if len(num_list) == 0:
            print(-1)

        else:
            print(num_list[-1])