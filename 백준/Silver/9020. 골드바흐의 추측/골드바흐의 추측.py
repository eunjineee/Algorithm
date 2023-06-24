import math
n = int(input())

def f(b):
    for j in range(2, int(math.sqrt(b))+1):
        if b % j == 0:
            return False
    return True


for i in range(n):
    a = int(input())
    h = a//2
    l = a//2
    while True:
        if f(h) and f(l):
            break
        else:
            h += 1
            l -= 1
    print(l, h)