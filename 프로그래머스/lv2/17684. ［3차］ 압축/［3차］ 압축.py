def solution(msg):
    answer = []

    di = {}
    for i in range(65,91):
        di[chr(i)] = i-64

    w = 0
    c = 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(di[msg[w:c]])
            break
        if msg[w:c+1] not in di.keys():
            di[msg[w:c+1]] = len(di)+1
            answer.append(di[msg[w:c]])
            w = c
    return answer