# 각 줄마다 행렬의 데이터를 입력받는 법법
a,b = map(int,input().split())

mylist = []
mylist_2 = []

# 각 줄 마다 '행'대로 입력을 받음
for i in range(a):
    mylist.append(list(map(int,input().split())))


# 두번째 행렬에 대해서도 각 줄마다 '행'대로 입력을 받음
for i in range(a):
    mylist_2.append(list(map(int,input().split())))



for k in range(0,a):
    for j in range(0,b):
        print(mylist[k][j] + mylist_2[k][j], end=' ')
    
    print()

