from collections import deque
n,m = map(int,input().split())
queue = deque([])
arr = [] 
visited = [[-1]*m for _ in range(n)]

for i in range(n):
    li = list(map(int, input().split(' ')))
    for j in range(m):
        if li[j] == 2:
            queue.append((i,j))
            visited[i][j] = 0
        elif li[j] == 0:
            visited[i][j] = 0
    arr.append(li)

direc = [(0,1),(1,0),(0,-1),(-1,0)]

while queue:
    (x,y) = queue.popleft()
    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == -1 and arr[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                arr[nx][ny] = 0

for i in visited:
    print(*i)