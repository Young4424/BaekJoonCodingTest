import sys
import math

n = int(sys.stdin.readline())

level_num = []

for i in range(n):
    number = int(sys.stdin.readline())
    level_num.append(number)


def merge_sort(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2

    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])


    merged_arr = []
    l = h = 0

    while l< len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l +=1

        else:
            merged_arr.append(high_arr[h])
            h +=1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr


# 절사평균 



def new_round(num):
    return math.floor(num+0.5)


n_average = new_round(n * 0.15)

level_num = merge_sort(level_num)

if n_average != 0:
    level_num = level_num[n_average:-n_average]


result = 0

for i in level_num:
    result +=i

if len(level_num) == 0:
    print(result)

else:
    avg = result/len(level_num)
    print(math.floor(avg + 0.5))

