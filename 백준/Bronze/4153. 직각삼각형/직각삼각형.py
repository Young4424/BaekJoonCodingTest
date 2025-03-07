while True:
    num_list = list(map(int,input().split()))

    num_list.sort()

    a = num_list[0]
    b = num_list[1]
    c = num_list[2]

    
 

    if a !=0 or b !=0 or c !=0:
        if c**2 == a**2 + b**2:
            print('right')
        else:
            print('wrong')

    else:
        break