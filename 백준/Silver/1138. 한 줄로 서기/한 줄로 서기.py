import sys
n = int(sys.stdin.readline())

list = list(map(int,sys.stdin.readline().split()))
list2= []
for m in range(n):
    list2.append((list[m],m+1))


li = [-1]*n
for i in range(n):
        a = -1
        for j in range(n):
            if li[j] == -1:
                a += 1
            if a == list2[i][0]:
                li[j] = list2[i][1]
                break
print(*li)