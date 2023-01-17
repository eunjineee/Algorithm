a,b,c= map(int, input().split())

def f(a,b,c):
    if b == 1:
        return (a%c)
    elif b%2 == 0:
        return (f(a,b//2,c)**2)%c
    else:
        return ((f(a,b//2,c)**2)*a)%c

print(f(a,b,c))