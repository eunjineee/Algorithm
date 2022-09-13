def ino(n):                                 # 중위순회
    if n:
        ino(ch1[n])
        print(par[n], end='')
        ino(ch2[n])

for S in range(1, 11):
    V = int(input())                        # 정점 개수, 마지막 정점 번호
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    par = [0] * (V + 1)                     # 노드에 해당하는 문자를 넣을 리스트

    for H in range(V):
        lst = list(input().split())
        if len(lst) == 4:                   # 자손이 둘일 때 
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])
        elif len(lst) == 3:                 # 자손이 하나일 때 
            ch1[int(lst[0])] = int(lst[2])
        par[int(lst[0])] = lst[1]

    print(f'#{S}', end=' ')
    ino(1)
    print()