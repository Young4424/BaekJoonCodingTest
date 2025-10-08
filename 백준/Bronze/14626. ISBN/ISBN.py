import sys

"""
ISBN

a, 3b, c , 3d, e, 3f, g, 3h, i , 3j, k, 3l, m

m = 10 - (a+3b+c+3d+e+3f+g+3h+i+3j+k+3l) mod 10

홀수(인덱스는 짝수)일 때 가중치 1, 짝수(인덱스는 홀수)일 때 가중치 3을 곱해준다.


"""


ISBN_number = str(sys.stdin.readline().strip())


star_loc = 0
sum = 0

# 별표 위치 확인하기

for i in range(0,13):
    if ISBN_number[i] == '*':
        star_loc = i
        continue

    else:
        if i % 2 == 0:
            sum += int(ISBN_number[i])

        else:
            sum += 3 * int(ISBN_number[i])


# * 공간에 숫자 하나씩 집어 넣어서 확인하기

for k in range(10):
    if star_loc % 2 == 0:
        if (k + sum) % 10 == 0:
            print(k)
            break

        else:
            continue

    else:
        if (3*k + sum) % 10 == 0:
            print(k)
            break

        else:
            continue






