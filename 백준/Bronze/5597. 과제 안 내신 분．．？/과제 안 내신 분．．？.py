student = []

for item in range(0,28):
    a = int(input())
    student.append(a)


for i in range(1,31):
    if i not in student:
        print(i)