T =int(input())

for t in range(T):
    nums=[]
    c = int(input())   # 점 개수
    for _ in range(c):
        x, y, d, e = map(int, input().split())
        nums.append([x,y,d,e])
    # print(f'nums:{nums}')

    ans = 0
    while len(nums) >= 2:    
        boom = {}  #겹치는 거 확인하는 용도
        deli = []
        for point in nums:
            direction = [(0,0.5),(0,-0.5),(-0.5,0),(0.5,0)] 
            #print(f'point: {point}')
            if -1000 <= point[0] + direction[point[2]][0] <= 1000 and -1000 <= point[1] + direction[point[2]][1] <= 1000:
                point[0] = point[0] + direction[point[2]][0]
                point[1] = point[1] + direction[point[2]][1]
                #print(f'change:{point}')
                if (point[0],point[1]) in boom.keys():
                    if (point[0],point[1]) not in deli:
                        boom[(point[0],point[1])] += point[3]
                        ans += boom[(point[0],point[1])]
                        # print(f'으악 {ans}')
                        deli.append((point[0],point[1]))
                    else:
                        ans += point[3]
                        # print(f'Rm악 {ans}')
                    # print(f'point:{(point[0],point[1])}')
                    # print(f'+:{boom[(point[0],point[1])]}')
                    # print(f'ans:{ans}')
                    # print(nums)
                else:
                    boom[(point[0],point[1])] = point[3]
            else:
                deli.append((point[0],point[1]))
        #print(f'nums:{nums}')
        if len(deli) != 0:
            for k in deli:
                a = 0
                while a < len(nums):
                    if (nums[a][0],nums[a][1]) == (k[0],k[1]):
                        nums.remove(nums[a])
                        a-=1
                    a += 1
                    
    print(f'#{t+1} {ans}')
    # print(nums)