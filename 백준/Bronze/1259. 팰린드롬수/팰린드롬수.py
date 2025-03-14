import sys

numbers = []

while True:
    # 입력을 받아 줄바꿈 문자를 제거합니다.
    line = sys.stdin.readline().strip() #strip은 줄바꿈을 제거하기 위함

    # 종료 조건 심사
    if line == '0':
        break

    # 입력 받은 값을 문자열로 변환하여 리스트에 추가
    numbers.append(str(line))


for item in numbers:

    number_letter = item
    reversed_letter = []

    for letter in reversed(number_letter):
        reversed_letter.append(letter)


    is_palndrom = True

    for i in range(len(number_letter)):
        if number_letter[i] == reversed_letter[i]:
            pass
        else:
            is_palndrom = False
            break


    if is_palndrom == True:
        print('yes')

    else:
        print('no')

