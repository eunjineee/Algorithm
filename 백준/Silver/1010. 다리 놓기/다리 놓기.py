t = int(input())
def fac(x):
    ans = 1
    for i in range(1,x+1):
        ans *= i
    return ans

for _ in range(t):
    n, m = map(int,input().split())
    a = max(n,m)
    b = min(n,m)

    answer = fac(a)//(fac(a-b)*fac(b))
    print(answer)