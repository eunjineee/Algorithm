def solution(today, terms, privacies):
    tdi = {}
    answer = []
    today =list(map(int,today.split('.')))
    for t in terms:
        ta, tb = t.split(' ')
        tdi[ta] = int(tb)
    for i in range(len(privacies)):
        bday, btype = privacies[i].split(' ')
        day = list(map(int,bday.split('.')))
        dayyy = day[1]+tdi[btype]
        while dayyy > 12:
            day[0] = day[0] + 1
            dayyy = dayyy -12    
        day[1] = dayyy
        print('today',today,'   day',day)
        if today[0] > day[0]:
            answer.append(i+1)
        elif today[0] == day[0]:
            if today[1] > day[1]:
                answer.append(i+1)
            elif  today[1] == day[1]:
                if today[2] >= day[2]:
                    answer.append(i+1)
    return answer
