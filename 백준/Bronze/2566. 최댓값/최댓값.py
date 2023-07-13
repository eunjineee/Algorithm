li = []

for i in range(9):
    li.append(list(map(int,input().split(' '))))

answer = (0,0,0)
for i in range(9):
    for j in range(9):
        if answer[0] < li[i][j]:
            answer = (li[i][j],i,j)

print(answer[0])
print(answer[1]+1,answer[2]+1)