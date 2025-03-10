def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        # 첫번째가 0이면 1로 만들기 위해 뒤집기가 필요
        count_to_all_one +=1
        # 첫번째가 1이면 0으로 만들기 위해 뒤집기 필요 
    elif string[0] == '1':
        count_to_all_zero +=1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == '0':
                count_to_all_one +=1

            if string[i+1] == '1':
                count_to_all_zero +=1

    return min(count_to_all_one,count_to_all_zero)



enter = str(input())
result = find_count_to_turn_out_to_all_zero_or_all_one(enter)

print(result)