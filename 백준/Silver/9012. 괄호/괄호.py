import sys



n = int(sys.stdin.readline().strip())

# 괄호가 텅 비어 있어야 올바른 문자열, Yes
# 남거나, 부족하면 No



for _ in range(n):
    vps_letter = str(sys.stdin.readline().strip())
    vps_stack = []

    for letter in vps_letter:
        if letter == '(':
            vps_stack.append(letter)

        elif letter == ')':
            if len(vps_stack) ==0:
                vps_stack.append(')')
                break

            else:
                vps_stack.pop()

    if len(vps_stack) !=0:
        print('NO')

    else:
        print('YES')




