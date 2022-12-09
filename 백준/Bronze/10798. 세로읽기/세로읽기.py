total = []
abc = [0 for i in range(5)]
ans = ''

for j in range(5):
    a = list(input())
    total.append(a)

while total:
    if abc == [1,1,1,1,1]:
        break
    for k in range(5):
        if len(total[k]) == 0:
            abc[k] = 1
        else:
            ans += total[k].pop(0)

print(ans)