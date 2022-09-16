
from collections import deque

def rec(a,i,j):
    queue.append((i,j))
    # visited = [[0]*a for _ in range(a)]
    # visited[i][j] = 1
    tutu = 1
    while queue:
        i, j = queue.popleft()
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di, j+dj
            if 0 <= ni < a and 0 <= nj < a and nums[ni][nj] == nums[i][j] + 1:
                queue.append((ni,nj))
                # visited[ni][nj] = visited[i][j] + 1
                tutu += 1
                    
    return tutu

T = int(input())

for t in range(T):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    total = {}
    queue = deque()
    for i in range(n):
        for j in range(n):
            heyhey = rec(n, i, j)
            if heyhey not in total.keys():
                total[heyhey] = nums[i][j]
            else:
                if total[heyhey] > nums[i][j]:
                    total[heyhey] = nums[i][j]


    ans1 = max(total.keys())
    ans2 = total[ans1]
    
    print(f'#{t+1} {ans2} {ans1}')
