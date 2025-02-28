T = int(input())

for test in range(T):
    num, letter = map(str,input().split())
    
    for alphabet in letter:
        print(int(num)*alphabet,end="")
    print()
