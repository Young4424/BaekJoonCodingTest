a,b = map(int, input().split())

c = list(map(int,input().split()))

result = []

for i in c:
    if i < b:
        result.append(i)

print(*result) # 리스트 요소 한번에 출력하기