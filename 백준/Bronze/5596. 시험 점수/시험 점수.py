a = list(map(int,(input().split(' '))))
b = list(map(int,(input().split(' '))))

anum = sum(a)
bnum = sum(b)

if anum >= bnum:
    print(anum)
else:
    print(bnum)