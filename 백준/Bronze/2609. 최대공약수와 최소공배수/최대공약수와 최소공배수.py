a,b = map(int,input().split())



def gcd(a,b):
    if a % b == 0: # b가 a를 나누면
        return b    # b가 최대 공약수
    
    elif b == 0:    # b가 0이면
        return a    # a가 최대 공약수
    
    else:
        # gcd(a,b) = gcd(b, a mod b) 적용
        return(gcd(b, a % b))
    
def lcm(a,b):
    return a * b // gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))