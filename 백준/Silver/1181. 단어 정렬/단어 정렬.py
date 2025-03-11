import sys

num = int(sys.stdin.readline().strip())

word_list = set([])

for item in range(num):
    new_word = str(sys.stdin.readline().strip())
    word_list.add(new_word)

word_list = list(word_list)
word_list.sort(key=lambda x: (len(x),x),reverse=False)

for item in word_list:
    print(item)
    