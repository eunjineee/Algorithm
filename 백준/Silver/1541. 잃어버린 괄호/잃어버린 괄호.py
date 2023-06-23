arr = list(input().split('-'))
arr2 = []
for i in arr:
    ans = 0
    for j in i.split('+'):
        ans += int(j)
    arr2.append(ans)

answer = arr2[0]
for a in arr2[1:]:
    answer -= a

print(answer)