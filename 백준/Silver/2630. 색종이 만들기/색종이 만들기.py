n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]

ans = []

def f(x,y,n):
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                f(x, y, n//2)
                f(x, y+n//2, n//2)
                f(x+n//2, y, n//2)
                f(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        ans.append(0)
    else:
        ans.append(1)

f(0,0,n)
print(ans.count(0))
print(ans.count(1))