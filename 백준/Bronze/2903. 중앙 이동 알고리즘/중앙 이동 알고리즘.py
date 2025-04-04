import sys

"""

한 변당 2개 점 / 전체 4개의 점

2 / 4 
        1 2^0
3 / 9
            2 ^ 1
5 / 25
                4 2^2
9 / 81

                    8

                        16


a0 = 2
n = 1:

a1 = (a0 + 2^(n-1)) =3 

n = 2

a2 = (a1 + + 2^1) =  5


a3 = (a2 +  2^2) = 9

..

an+1 = (an +  2^n-1)


"""

n = int(sys.stdin.readline().strip())


a_0 = 2
result = 0

for i in range(1,n+1):
    new_a1 = a_0 + 2**(i-1)
    result = new_a1**2
    a_0 = new_a1


print(result)