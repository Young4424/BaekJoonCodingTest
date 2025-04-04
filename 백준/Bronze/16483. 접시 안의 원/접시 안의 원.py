import sys

n = int(sys.stdin.readline().strip())

"""
a^2 = (T/2)^2 + b^2 , 접선이 원의 중점으로부터 수직이므로, a가 가장 긴 빗변이 된다.

그래서 a^2 - b^2 = (T/2)^2


"""


result = round((n/2)**2)

print(result)