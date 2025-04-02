import sys


T,S = map(int,sys.stdin.readline().split())


# 술하고 같이 먹거나, 점심 식사가 아닐 경우에 280개

if S == 1:
    print(280)


else:
    # 점심식사 + 술과 같이 안 먹음음
    if 12<=T<=16:
        print(320)

    else:
        print(280)