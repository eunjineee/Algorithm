n = int(input())
li = [1] *10

for i in range(n):
    for j in range(1,10):
        li[j] = li[j] + li[j-1]

print(li[-1]%10007)