n = int(input())

dict = {}

for i in range(n):
    w = list(input())
    w.sort()
    m = ''.join(w)
    if m in dict:
        dict[m] += 1
    else:
        dict[m] = 1

ans = len(dict.keys())
print(ans)