import sys
sum = 0

for _ in range(5):
    score = int(sys.stdin.readline().strip())
    if score < 40:
        sum += 40

    else:
        sum +=score


print(int(sum/5))