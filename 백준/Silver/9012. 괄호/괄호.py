n = int(input())

for i in range(n):
    stack=[]
    data = input()
    ans = True
    for j in data:
        if j == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                ans = False
            else:
                stack.pop(-1)
    if len(stack) != 0 or ans == False:
        print('NO')
    else:
        print('YES')