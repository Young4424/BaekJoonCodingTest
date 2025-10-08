import sys


word = str(sys.stdin.readline().strip())

alphabet_count = [0 for i in range(26)]



for letter in word:
    number = ord(letter)
    count = 0

    for chr_num in range(97,123):
        if chr_num == number:
            alphabet_count[count] += 1
            count+=1

        else:
            count+=1


for item in alphabet_count:
    print(item, end=" ")



    
