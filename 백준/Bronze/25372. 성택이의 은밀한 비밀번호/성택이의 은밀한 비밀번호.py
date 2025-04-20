import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    try:
        password = sys.stdin.readline().strip()
        
        if len(str(password))>=6 and len(str(password))<=9:
            print('yes')

        else:
            print('no')
    
    except:
        print('no')