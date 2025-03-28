import sys

n = int(sys.stdin.readline())

num_list = []
for _ in range(n):
    number = int(sys.stdin.readline())
    
    if number != 0:
        num_list.append(number)

    else:
        if len(num_list) == 0:
            num_list.append(number)

        else:
            del num_list[-1]

result = 0

for item in num_list:
    result +=item

print(result)