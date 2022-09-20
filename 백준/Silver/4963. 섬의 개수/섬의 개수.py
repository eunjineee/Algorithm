import sys
sys.setrecursionlimit(100000000)
def hey(x,y):
    nums[y][x] = 0
    d = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]] 
    for dd in d:
        ny = y + dd[0]
        nx = x + dd[1]
        if w > nx >= 0 and h > ny >= 0 and nums[ny][nx] == 1:
            hey(nx, ny)

while True:
    w, h =  map(int,(input().split()))
    if w == 0 and h == 0:
        break
    nums = [list(map(int, input().split()))+[0] for _ in range(h)]
    
    ans = 0
    for j in range(h):
        for i in range(w):
            if nums[j][i] == 1:
                hey(i,j)
                ans += 1
    print(ans)