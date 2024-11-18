a = int(input())
b = int(input())
minab = min(a,b)
def gcd(a,b):
    for i in range(minab,0,-1):
        if a % i == 0 and b % i == 0:
            print(i)
            break

print(gcd(a,b))
