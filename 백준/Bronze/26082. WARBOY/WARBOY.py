import sys


"""

WARBOY는 가격 대비 성능이 경쟁사 제품 대비 3배

가격 대비 성능 =  성능 / 가격

WARBOY의 성능 =  (3 * (경쟁사 성능 / 경쟁사 가격)) * WARBOY 가격


"""


A,B,C = map(int,sys.stdin.readline().split())


Warboy_performance = (3* (B/A)) * C

print(int(Warboy_performance))

