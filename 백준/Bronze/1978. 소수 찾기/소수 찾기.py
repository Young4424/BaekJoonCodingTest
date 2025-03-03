num = int(input())
numbers = list(map(int,input().split()))
count = 0

for item in numbers:
    if item == 1:
        continue

    for test in range(2,item):
        if (item%test) == 0:
            break

    else:
        count +=1


print(count)
