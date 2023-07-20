import math

def f(a):
    num = 1
    for i in range(1, a+1):
        num *= i
    return num

def solution(n):
    one = n
    two = 0
    ans = 0
    while one >= 0:
        ans += f(one+two)//(f(one)*f(two))
        one -= 2
        two += 1
    
    return ans%1234567