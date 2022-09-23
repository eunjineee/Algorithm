import sys
input = sys.stdin.readline

n = int(input())
nli = list(map(int,input().split()))  #배
m = int(input())
mli = list(map(int, input().split()))  #짐
nli.sort(reverse=True)
mli.sort(reverse=True)  #짐 큰거~ 작은거


ans = 0
while len(mli) != 0 and len(nli):
    if max(mli) > max(nli):
        ans = -1
        break
    for i in nli:
        for j in mli:
            if i >= j :
                mli.remove(j)
                break
    ans+= 1
print(ans)
