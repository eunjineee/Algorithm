N = int(input())
pwd = input()
ans = 0
anum = ord('a')
N -= 1
for alpha in pwd:
    diff = ord(alpha) - anum
    if diff > 0:
        ans += (diff)*26*(26**N-1)//(25) + diff
    ans += 1
    N -= 1
print(ans)