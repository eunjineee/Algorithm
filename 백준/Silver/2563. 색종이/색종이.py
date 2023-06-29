n = int(input())
paper = [['0' for i in range(100)]for j in range(100)]

for _ in range(n):
    a, b = map(int, input().split())
    for k in range(a-1,a+9):
        for l in range(b-1,b+9):
            paper[k][l] = '1'
ans = 0
for aa in range(100):
    for bb in range(100):
        if paper[aa][bb] == '1':
            ans += 1

print(ans)