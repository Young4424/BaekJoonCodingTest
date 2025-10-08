import sys

word_list = list(map(str,sys.stdin.readline().split()))


ban_word = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

can_use_word = [word_list[0]]



# 첫번쨰 단어는 중요하므로, 금지된 단어여도 미리 추가해놓은 후, index 1부터 시작
for count in range(1,len(word_list)):
    if word_list[count] in ban_word:
        continue

    else:
        can_use_word.append(word_list[count])



for word in can_use_word:
    print(word[0].upper(),end="")