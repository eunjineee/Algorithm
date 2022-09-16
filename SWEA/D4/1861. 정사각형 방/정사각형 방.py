
from collections import deque

def rec(i,j):
    queue.append((i,j))
    # visited = [[0]*a for _ in range(a)]
    # visited[i][j] = 1
    tutu = 1
    while queue:
        i, j = queue.popleft()
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n:
                if nums[ni][nj] == nums[i][j] + 1:
                    queue.append((ni,nj))
                    # visited[ni][nj] = visited[i][j] + 1
                    tutu += 1                   
    return tutu

T = int(input())

for t in range(T):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    ans1 = 0
    ans2 = 0
    queue = deque()
    for i in range(n):
        for j in range(n):
            heyhey = rec(i, j)
            if heyhey > ans1: 
                ans1 = heyhey
                ans2 = nums[i][j]
            elif heyhey == ans1:
                if ans2 > nums[i][j]:
                    ans2 = nums[i][j]

    # ans1 = max(total.keys())
    # ans2 = total[ans1]
    
    print(f'#{t+1} {ans2} {ans1}')
