from collections import deque


n,m = map(int,input().split())
arr = []
answer = [[-1]*m for _ in range(n)]
ans = 0

for i in range(n):
    word = list(input())
    arr.append(word)
    for j in range(m):
        if word[j] == 'I':
            start = (i,j)
        elif word[j] == 'X':
            answer[i][j] = 0

dd = [(0,1),(1,0),(0,-1),(-1,0)]
queue = deque([start])

while queue:
    (x,y) = queue.popleft()
    for dx,dy in dd:
        nx,ny = x+dx, y+dy 
        if 0<= nx < n and 0 <= ny < m and answer[nx][ny] == -1:
            answer[nx][ny] = 0
            if arr[nx][ny] == 'P':
                ans += 1
            queue.append((nx,ny))

if ans:
    print(ans)
else:
    print('TT')