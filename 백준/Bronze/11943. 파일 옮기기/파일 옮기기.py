a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())

if a1+b2 <= a2+b1:
    print(a1+b2)
else:
    print(a2+b1)