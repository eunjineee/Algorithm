m = int(input())
d = int(input())

if m == 2:
    if d > 18:
        print('After')
    elif d == 18:
        print('Special')
    else:
        print('Before')
elif m > 2:
    print('After')
else:
    print('Before')