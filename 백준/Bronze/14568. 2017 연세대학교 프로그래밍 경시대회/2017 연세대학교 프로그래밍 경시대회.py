candy = int(input())

# A : 택희
# B : 영훈이
# C : 남규

count = 0 # 사탕 세기

for A in range(0,candy+1):
    for B in range(0,candy+1):
        for C in range(0,candy+1): # A,B,C는 각각 0~6개를 받을 수 있다.
            if (A + B + C) == candy:    # 조건 1 : 남는 사탕은 없어야 한다.

                # 조건 2,4: 남규는 영훈이보다 2개 이상 가지기, 택희 사탕은 짝수개
                if C >= B+2 and A % 2 == 0:

                    # 조건 3 : 셋중 사탕을 0개 받는 사람은 없어야 함
                    if A !=0 and B !=0 and C !=0: 
                        count +=1                
                        

print(count)