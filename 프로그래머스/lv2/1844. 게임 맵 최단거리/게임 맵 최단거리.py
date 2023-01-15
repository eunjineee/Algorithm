answer = 10**5

def solution(maps):
    global answer 
    h = len(maps)
    w = len(maps[0])
    q = []
    visited = [[1]*w for _ in range(h)]
    def f(x,y):
        q.append((x,y))
        while q:
            (x, y) = q.pop(0)
            global answer 
            if x == h-1 and y == w-1:
                if answer > visited[x][y]:
                    answer = visited[x][y]
            else:
                for d in [(-1,0),(0,-1),(0,1),(1,0)]:
                    nx,ny = x+d[0], y+d[1]
                    if 0 <= nx < h and 0 <= ny < w:
                        if maps[nx][ny] == 1 and visited[nx][ny] == 1:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx,ny))
    f(0,0)
    if answer == 10**5:
        return -1
    else:
        return answer