T = int(input())
arr = []
for _ in range(T):
    a,b = map(int, input().split())
    arr.append((b,a))
arr.sort()
q = arr[0][0]
result = 1
for i in range(1,T):
    if arr[i][1] >= q:
        result += 1
        q = arr[i][0]
print(result)