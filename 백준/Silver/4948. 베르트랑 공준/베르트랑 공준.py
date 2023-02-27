#python3
from math import sqrt
li = [False, True]
for i in range(2,246913):
        for j in range(2,int(sqrt(i))+1):
            if i % j == 0:
                li.append(False)
                break
        else:
            li.append(True)

while True:
    ans = 0
    n = int(input())
    if n == 0:
        break
    for k in range(n+1,2*n+1):
        if li[k] == True:
            ans += 1      
    print(ans)