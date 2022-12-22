n = int(input())
li = []
for i in range(n):
    if i == 0:
        a = list(input())
    else:
        li.append(list(input()))

if li:
    for j in li:
        for k in range(len(j)):
            if a[k] != j[k]:
                a[k] = '?'

print(''.join(a))