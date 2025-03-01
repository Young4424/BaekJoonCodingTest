word = str(input())

new_word = []

# 문자열은 수정이 불가능함

for index, letter in enumerate(word):
    if letter.upper() != letter:
        new_word.append(letter.upper()) 

    elif letter.lower() != letter:
        new_word.append(letter.lower())

    else:
        pass


for item in new_word:
    print(item,end='')