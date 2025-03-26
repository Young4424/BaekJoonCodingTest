import sys


word = sys.stdin.readline().strip()

count = 0

try:

    for i in range(len(word)):
        if word[i] == 'D':
            if word[i+1] == 'K':
                if word[i+2] == 'S':
                    if word [i+3] == 'H':
                        count +=1



    print(count)

except:
    print(count)

    

