def f(i, N):
    global  ans
    if i == N:
        s= 0                                   #부분 집합의 합
        for i in range(N):
            if bit[i]:
                s += 1
        if s == m:
            ans += 1                           #부분집합의 합이 10인 경우의 수
            for i in range(N):
                if bit[i]:
                    print(A[i], end = ' ')
            print()
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

n, m =map(int, input().split())
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * n
ans = 0
f(0, n)