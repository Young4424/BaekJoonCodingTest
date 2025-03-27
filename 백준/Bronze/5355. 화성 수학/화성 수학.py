import sys

n = int(sys.stdin.readline().strip())

result = 0

for _ in range(n):
    num_expression = list(map(str,sys.stdin.readline().split()))

    a = float(num_expression[0])

    for item in num_expression:
        if item == '@':
            a = a * 3

        elif item == '%':
            a = a + 5

        elif item == '#':
            a = a-7

        else:
            continue

    result = a
    print('%.2f' % result)


