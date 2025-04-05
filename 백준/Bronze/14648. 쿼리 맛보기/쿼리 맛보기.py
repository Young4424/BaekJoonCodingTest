import sys

n,q = map(int,sys.stdin.readline().split())

n_list = list(map(int,sys.stdin.readline().split()))

def swap(a,b):
    normal = a
    a= b
    b = normal
    return a,b


for _ in range(q):
    queue = list(map(int,sys.stdin.readline().split()))
    
    if queue[0] == 1:
        print(sum(n_list[queue[1]-1:queue[2]]))

        new_a, new_b = swap(n_list[queue[1]-1], n_list[queue[2]-1])

        n_list[queue[1]-1] = new_a
        n_list[queue[2]-1] = new_b

    elif queue[0] == 2:
        print(sum(n_list[queue[1]-1:queue[2]])-sum(n_list[queue[3]-1:queue[4]]))