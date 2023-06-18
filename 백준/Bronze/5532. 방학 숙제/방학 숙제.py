import math

l = int(input())

a = int(input())
b = int(input())
c = int(input())
d = int(input())

num = max(math.ceil(a/c),math.ceil(b/d))
print(l-num)