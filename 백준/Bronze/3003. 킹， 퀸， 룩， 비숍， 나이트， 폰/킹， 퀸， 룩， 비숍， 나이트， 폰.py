a = list(map(int,input().split()))
b = [1,1,2,2,2,8]
ans = []
for i in range(6):
    n = b[i] - a[i]
    ans.append(n)

print(*ans,sep=' ')