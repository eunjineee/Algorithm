from collections import deque

def f(c):
    stack = []
    for j in c:
        if j in ['[','{','(']:
            stack.append(j)
        else:
            if len(stack) != 0:
                stack_pop = stack.pop()
                if j == ']' and stack_pop != '[':
                    return 0
                elif j == '}' and stack_pop != '{':
                    return 0
                elif j == ')' and stack_pop != '(':
                    return 0
            else:
                return 0
    if len(stack) == 0 :
        return 1
    else:
        return 0

def solution(s):
    ans = 0
    li = deque(list(s))
    for _ in range(len(s)):
        li.rotate(-1)
        ans += f(li)
    return ans