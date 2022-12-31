import sys
input=sys.stdin.readline
n = int(input())
li = {}
for i in range(n):
    a, b = input().split()
    if b == 'enter':
        li[a] = 0
    else:
        del li[a]
li= sorted(li, reverse=True)

for j in li:
    print(j)