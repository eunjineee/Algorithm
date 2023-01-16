import sys
input = sys.stdin.readline
T = int(input().strip())

for t in range(T):
    n = int(input())
    li = []
    for m in range(n):
        li.append(input().strip())
    li.sort()
    for i in range(len(li)-1):
        ii = len(li[i])
        if li[i] == li[i+1][:ii]:
            print('NO')
            break
    else:
        print('YES')