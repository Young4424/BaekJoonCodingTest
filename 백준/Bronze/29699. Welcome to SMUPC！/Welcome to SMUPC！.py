import sys

letter = "WelcomeToSMUPC"

n = int(sys.stdin.readline().strip())


num = n % 14

print(letter[num-1])