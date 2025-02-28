while True:
    try:
        letter = input()
        num = int(input())

        print(letter[num-1])

    except:
        break