import sys

word = str(sys.stdin.readline().strip())
result = 0

dict = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

for letter in word:
    for dic_letter in dict:
        if letter in dic_letter:
            num = dict.index(dic_letter) + 3
            result += num


print(result)