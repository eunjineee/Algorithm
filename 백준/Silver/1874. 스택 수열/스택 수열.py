import sys
input = sys.stdin.readline
n = int(input())

nums = []
for i in range(n,0,-1):
    nums.append(i)

stack = []
total = []

for j in range(n):
    a = int(input())
    if a in nums:
        while a in nums:
            stack.append(nums.pop())
            total.append('+')
        stack.pop()
        total.append('-')
    elif len(stack) > 0 and stack[-1] == a:
        total.append('-')
        stack.pop()
    elif len(stack) > 0 and stack[-1] != a:
        print('NO')
        exit()

for k in total:
    print(k)
