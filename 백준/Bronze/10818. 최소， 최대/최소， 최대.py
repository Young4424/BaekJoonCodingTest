number = int(input())

a = list(map(int,input().split()))


a.sort()


print(f'{a[0]} {a[number-1]}')