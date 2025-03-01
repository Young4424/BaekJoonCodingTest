T_case = int(input())

for test in range(T_case):
    result_OX = str(input())

    score = 0
    total = 0
    for index, item in enumerate(result_OX):
        if item == 'O':
            # 수열 : a(n+1) = a(n) + 1
            score = score + 1
            total = total + score
        
        else:
            score = 0

    print(total)



    