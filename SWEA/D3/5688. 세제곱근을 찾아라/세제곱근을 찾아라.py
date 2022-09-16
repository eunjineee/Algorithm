T = int(input())

for t in range( T):
    n = int(input())

    num = n **(1/3)
    num = round(num)

    if num ** 3 == n:
        print(f'#{t+1} {num}')
    else:
        print(f'#{t+1} -1')
