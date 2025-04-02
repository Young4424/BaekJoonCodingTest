import sys

bread,pattie = map(int,sys.stdin.readline().split())


# 햄버거를 반환하는 최대 개수 


hamburger = 0

while True:
    bread = bread-2
    pattie = pattie - 1

    if bread < 0 or pattie <0:
        break


    else:
        hamburger +=1

print(hamburger)
