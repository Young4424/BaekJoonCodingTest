"""
설탕 배달

사탕가게에 Nkg 배달해야 한다.

봉지 : 3,5 kg

최대한 적은 봉지를 들고 가려함.

ex) 18kg = 5 * 3 + 3  / 3 * 6 (x)


정확하게 Nkg배달할 때, 봉지 몇개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오


18 = 5 *3 +1

4 = 3 * (x) -1

6 = 3 * 2


11 = 5 * 2 (x)


1) N을 5로 나눌 떄, 나누어 떨어지는 경우

2) N을 5로 나눌 때, 나머지가 있는 경우


2-1) 3kg씩 사용하면서서, 5로 나누어지는 경우가 있는 지 확인 

"""

import sys

a = int(sys.stdin.readline())
result = 0
origin_number = a

while a>0:
    if a % 5 == 0:
        result += int(a//5)
        a = 0
        break
    
    
    a = a-3
    result +=1


# 정확하게 nkg을 만들 수 있는 지 확인인
    if a < 0:
        result = -1

print(result)