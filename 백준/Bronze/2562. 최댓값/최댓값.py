c_list = []
index = 0 # 최댓값의 index 구하기
max = 0 # 최댓값 구하기

while True:
    try:
        a = int(input())
        c_list.append(a)

    # 공백이 들어오면 while문 break
    except:
        break


# Enumerate 함수 사용하기

for i, letter in enumerate(c_list):
    if max < letter:
        max = letter
        index = i+1 # 0부터 시작하므로 +1을 해주어야함

print(max)
print(index)

