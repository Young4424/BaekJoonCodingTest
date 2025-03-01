num = int(input())

# 수학적 규칙을 찾아야 함
for i in range(0,num):
    H,W,N = map(int,input().split())

    # 주기를 발견하기 위해서, 나눗셈을 활용하자

    if N % H == 0:
        floor = H
        room = N//H

    else:
        floor = N%H
        room = (N//H)+1


    print(f'{floor*100 + room}')