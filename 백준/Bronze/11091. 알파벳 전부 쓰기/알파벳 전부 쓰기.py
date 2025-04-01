import sys

n = int(sys.stdin.readline().strip())


def find_alphabet_occurence_array(string):
    alphabet_occurence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue

        char = char.lower()

        arr_index = ord(char) - ord('a')

        try:
            alphabet_occurence_array[arr_index] +=1

        except:
            pass

    return alphabet_occurence_array




for _ in range(n):
    sentence = str(sys.stdin.readline().strip(" "))
    result = find_alphabet_occurence_array(sentence)

    is_pangram = True
    loc_non_pangram = ""

    for index, item  in enumerate(result):
        if item == 0:
            is_pangram = False
            loc_non_pangram= loc_non_pangram+chr(index+97)


        else:
            continue

    if is_pangram == True:
        print('pangram')

    else:
        print('missing',loc_non_pangram)

    
