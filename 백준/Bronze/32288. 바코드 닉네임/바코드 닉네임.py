import sys

n = int(sys.stdin.readline().strip())

letter = sys.stdin.readline().strip()

letter_list = []

for i in range(n):
    if letter[i] == 'I':
        letter_list.append(letter[i].lower())

    elif letter[i] == 'l':
        letter_list.append(letter[i].upper())



print(''.join(letter_list))
