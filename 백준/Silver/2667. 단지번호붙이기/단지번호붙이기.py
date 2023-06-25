n = int(input())
li = []
mm = [['0' for k in range(n)] for g in range(n)]
ans = 0

for _ in range(n):
    li.append(list(input()))

def f(a,b,c):
    mm[a][b] = c
    dd = [(0,1),(1,0),(0,-1),(-1,0)]
    for d in dd:
        a1 = a + d[0]
        b1 = b + d[1]
        if 0<=a1<n and 0<=b1<n:
            if mm[a1][b1] == '0' and li[a1][b1] == '1':
                f(a1,b1,c)
answer = []

c = 1
for i in range(n):
    for j in range(n):
        if mm[i][j] == '0' and li[i][j] == '1':
            f(i,j,c)
            c += 1
            ans += 1

print(ans)

for l in range(1,ans+1):
    answer1 = 0
    for o in mm:
        answer1 += o.count(l)
    answer.append(answer1)
print(*sorted(answer))