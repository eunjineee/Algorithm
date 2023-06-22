from itertools import product

n, r = map(int, input().split())
a = [i for i in range(1,n+1)]
for cwr in product(a, repeat=r):
    print(*cwr)