import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    num_list = [str(i) for i in range(a,b+1)]
    count = 0
    for item in num_list:
        count += item.count('0')
           
    print(count)
