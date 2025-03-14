import sys

N = int(sys.stdin.readline().strip())

word = str(sys.stdin.readline().strip())

num_result = []

for letter in word:
    result = ord(letter) - ord('a') + 1 # +1은 a가 1이여야 하므로 더해준다.
    num_result.append(result)


sum = 0

for index, item in enumerate(num_result):
    sum += (item * (31**index))


hash = sum % 1234567891
print(hash)