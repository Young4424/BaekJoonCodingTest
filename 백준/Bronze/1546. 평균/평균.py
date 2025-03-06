import sys
number = int(input())
score_list = list(map(int,input().split()))

M = max(score_list)

adjust_sum = 0
for item in score_list:
    adjust_sum += (item/M) * 100


average = adjust_sum / number

print(average)
