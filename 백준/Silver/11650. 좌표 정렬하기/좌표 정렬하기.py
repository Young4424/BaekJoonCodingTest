import sys

N = int(sys.stdin.readline())

numbers = []

for _ in range(N):

    # 입력을 받아 줄바꿈 문자를 제거합니다.
    x,y = map(int,sys.stdin.readline().split()) #strip은 줄바꿈을 제거하기 위함

    numbers.append((x,y))

numbers.sort()


for a,b, in numbers:
    print(a,b)


