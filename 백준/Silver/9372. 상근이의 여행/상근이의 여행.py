from sys import stdin

T = int(stdin.readline())

course = []
airplane = []
for i in range(T) : 
    course.append(list(map(int, stdin.readline().split())))
    t = []
    for j in range(course[i][1]) :
        t.append(list(map(int, stdin.readline().split())))
    airplane.append(t)

for i in range(T) :
    print(course[i][0]-1)