result = []
for num in range(0,10):
    a = int(input())
    result.append(a%42)

unique_list = []

for item in result:
    if item not in unique_list:
        unique_list.append(item)

    

print(len(unique_list))
