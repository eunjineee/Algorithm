def solution(n):
    answer = []
    num = 0 
    for i in range(1,n+1):
        answer.append([0]*i+[-1]*(n-i))
        num += i
    # print(num)
    # print(answer)
    a,b = 0,0
    d = 0
    dd = [(1,0),(0,1),(-1,-1)]
    answer[0][0] = 1
    for i in range(2, num+1):
        if 0<=a+dd[d][0]<n and 0<=b+dd[d][1]<n:
            a,b = a+dd[d][0], b+dd[d][1]
            if answer[a][b] == 0:
                answer[a][b] = i
                # print(answer)
            else:
                if d == 2:
                    d = 0
                    # a,b = a+2, b+1
                    a,b = a-dd[d-1][0]+dd[d][0], b-dd[d-1][1]+dd[d][1]
                    answer[a][b] = i
                    # print(answer)
                else:
                    d += 1
                    a,b = a-dd[d-1][0]+dd[d][0], b-dd[d-1][1]+dd[d][1]
                    answer[a][b] = i
                    # print(answer)
        else:
            if d == 2:
                d = 0
            else:
                d += 1
                a,b = a+dd[d][0], b+dd[d][1]
                answer[a][b] = i
                # print(answer)
        
    totalans = []
    for ans in answer:
        for s in ans:
            if s != -1:
                totalans.append(s)

    return totalans