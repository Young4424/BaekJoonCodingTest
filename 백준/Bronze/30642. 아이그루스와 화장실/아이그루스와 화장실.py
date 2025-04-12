import sys


"""

1~N층까지 복층층

홀수층 - 몸집이 큰 동물

짝수 - 작은 동물

안뇽이 - 용
인덕 - 오리

자신의 몸집에 맞는 가장 가까운 화장실은?


동아리 방의 층수 N



"""


n = int(sys.stdin.readline().strip())
animal = str(sys.stdin.readline().strip())
present_floor = int(sys.stdin.readline().strip())



if animal == 'annyong':
    if present_floor % 2 == 0:
        present_floor +=1

        if present_floor > n:
            present_floor -=2
        


elif animal == 'induck':
    if present_floor % 2 !=0:
        present_floor +=1
        
        if present_floor > n:
            present_floor -=2


        

print(present_floor)

