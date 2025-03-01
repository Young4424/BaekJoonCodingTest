word = str(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'


for letter in alphabet:
    if letter in word:
        print(word.index(letter), end= ' ')

    else:
        print(-1, end=' ')