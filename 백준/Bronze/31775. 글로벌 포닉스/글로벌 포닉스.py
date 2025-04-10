import sys

starts_with_l = False
starts_with_k = False
starts_with_p = False


for _ in range(3):
    word = str(sys.stdin.readline().strip())

    if word[0] == 'l':
        starts_with_l = True

    elif word[0] == 'k':
        starts_with_k = True

    elif word[0] == 'p':
        starts_with_p = True



if starts_with_p and starts_with_l and starts_with_k :
    print('GLOBAL')

else:
    print('PONIX')