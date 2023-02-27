from math import sqrt
while True:
    ans = 0
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n+1,2*n+1):
            for j in range(2,int(sqrt(i))+1):
                if i % j == 0:
                    break
            else:
                ans += 1
        print(ans)