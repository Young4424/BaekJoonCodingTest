# 백준 2503번 - 숫자 야구
test = int(input())
hints = [list(map(int, input().split())) for _ in range(test)]
answer = 0

# 가능한 모든 3자리 수에 대해 확인
for a in range(1, 10):  # 100의 자리
    for b in range(1, 10):  # 10의 자리
        if b == a:  # 같은 숫자는 사용 불가
            continue
        for c in range(1, 10):  # 1의 자리
            if c == a or c == b:  # 같은 숫자는 사용 불가
                continue
            
            # 현재 숫자 (abc)
            num = a * 100 + b * 10 + c
            num_str = str(num)
            
            # 모든 힌트를 만족하는지 확인
            valid = True
            for hint in hints:
                guess, strike_expected, ball_expected = hint
                guess_str = str(guess)
                
                strike = 0
                ball = 0
                
                # 스트라이크 계산
                for i in range(3):
                    if guess_str[i] == num_str[i]:
                        strike += 1
                
                # 볼 계산
                for i in range(3):
                    if guess_str[i] in num_str and guess_str[i] != num_str[i]:
                        ball += 1
                
                # 계산된 결과가 힌트와 일치하는지 확인
                if strike != strike_expected or ball != ball_expected:
                    valid = False
                    break
            
            # 모든 힌트를 만족하면 정답 개수 증가
            if valid:
                answer += 1

print(answer)