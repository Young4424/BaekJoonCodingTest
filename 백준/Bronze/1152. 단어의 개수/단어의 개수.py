sentence = str(input())

a = sentence.split(' ')

while '' in a:
    a.remove('')


# 리스트 요소의 개수 세기
print(len(a))
