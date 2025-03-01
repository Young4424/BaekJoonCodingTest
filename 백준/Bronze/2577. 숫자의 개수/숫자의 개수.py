a = int(input())
b = int(input())
c = int(input())

mul = a*b*c

mul_string = str(mul)



for number in range(0,10):
    count = 0
    for item in mul_string:
        if str(number) in item:
            count +=1

    print(count)


    