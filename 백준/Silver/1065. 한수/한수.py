n = int(input())
ans = 0

def f(a):
    b = str(a)
    c = int(b[0]) - int(b[1])
    for j in range(1,len(b)-1):
        if int(b[j])-int(b[j+1]) != c:
            return 0
    return 1

for i in range(1, n+1):
    if i <= 99:
        ans +=1
    else:
        ans += f(i)

print(ans)