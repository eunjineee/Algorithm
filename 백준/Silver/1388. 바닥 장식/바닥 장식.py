n, m = map(int, input().split())
room = []
for k in range(n):
    room.append(list(input()))

li = [['0' for _ in range(m)] for v in range(n)]
dd = [(0,1),(1,0)]

def f(a,b):
    li[a][b] = '1'
    
    if room[a][b] == '-':
        t = 0
    else:
        t = 1
    a1 = a + dd[t][0]
    b1 = b + dd[t][1]
    if 0<=a1<n and 0<=b1<m:
      if room[a][b] == room[a1][b1]:
          f(a1,b1)
ans = 0
for i in range(n):
    for j in range(m):
        if li[i][j] == '0':
            f(i,j)
            ans += 1

print(ans)