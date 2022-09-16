def f(i, N, b):
    if i == N:
        s= 0                                   
        for i in range(N):
            if bit[i]:
                s += A[i]
        if s >= b:
            num = 0                        
            for i in range(N):
                if bit[i]:
                    num += A[i]
            totallist.append(num)
    else:
        bit[i] = 1
        f(i+1, N, b)
        bit[i] = 0
        f(i+1, N, b)

T= int(input())
for tt in range(T):
    n, b = map(int, input().split())
    A = list(map(int, input().split()))

    bit = [0] * (n+1)
    totallist = []
    f(0, n, b)
    ans = min(totallist) - b
    print(f'#{tt+1} {ans}')