import sys

T = str(sys.stdin.readline().strip())

i = 0
while i < (len(T)):
    print(T[i:i+10])
    i = i+10