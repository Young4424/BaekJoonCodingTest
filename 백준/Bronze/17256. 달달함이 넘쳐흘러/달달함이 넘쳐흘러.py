import sys

"""
x,y,z : 자연수 순서쌍
a.x, a.y, a.z : 케이크 수


# a = b의 의미

a.x = b.x , a.y = b.y, a.z = b.z


# a 케이크 b 연산

a 케이크 b = (a.z + b.x, a.y * b.y, a.x + b.z) = (c.x, c.y, c.z)



a.z + b.x = c.x ,  b.x = c.x - a.z
a.y * b.y = c.y ,  b.y = c.y / a.y
a.x + b.z = c.z ,  b.z = c.z - a.x





"""


a_x, a_y, a_z = map(int,sys.stdin.readline().split())
c_x, c_y, c_z = map(int,sys.stdin.readline().split())


b_x = c_x - a_z
b_y = int(c_y / a_y)
b_z = c_z - a_x

print(b_x, end= " ")
print(b_y, end= " ")
print(b_z, end= " ")