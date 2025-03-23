import sys

N = int(sys.stdin.readline())

num_list = list(map(int,sys.stdin.readline().split()))

    
M = int(sys.stdin.readline())

number = list(map(int,sys.stdin.readline().split()))


num_list.sort()


def lower_bound(nums,target):
    left,right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid +1

        else:
            right = mid

    return left


def upper_bound(nums,target):
    left, right = 0, len(nums)

    while left < right:

        mid = (left+right) // 2

        if nums[mid] <= target:
            left = mid +1

        else:
            right = mid

    return left
    

for item in number:
    count = 0
    count = upper_bound(num_list,item) - lower_bound(num_list,item)
    print(count,end=" ")