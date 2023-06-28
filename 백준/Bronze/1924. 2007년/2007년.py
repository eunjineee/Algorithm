li = [0,31,28,31,30,31,30,31,31,30,31,30,31]
dayen = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
m, d = map(int, input().split())
day = 0


for i in range(1,m):
    day += li[i]
day += d

print(dayen[day%7])