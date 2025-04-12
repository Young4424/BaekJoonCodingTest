import sys

# 행 a 열 b

n,a,b = map(int,sys.stdin.readline().split())

all_list = []

num_list = []

for i in range(n):
    num_list = list(map(int,sys.stdin.readline().split()))

    all_list.append(num_list)


jinsu = all_list[a-1][b-1]

is_happy = True


# 열은 고정, 행은 바뀜
for i in range(n):
    if all_list[i][b-1] > jinsu:
        is_happy = False



for j in range(n):
    if all_list[a-1][i] > jinsu:
        is_happy = False


if is_happy == False:
    print('ANGRY')

else:
    print('HAPPY')