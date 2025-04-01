import sys

n = int(sys.stdin.readline())

vowels = ['a','e','i','o','u','A','E','I','O','U']

for _ in range(n):
    sentence = sys.stdin.readline().split()
    vowel_count = 0
    non_vowel_count = 0

    for word in sentence:
        for letter in word:
            if letter in vowels:
                vowel_count +=1

            else:
                non_vowel_count +=1
        


    print(non_vowel_count,vowel_count)

