import math

def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        answer.append(math.ceil((100-progresses[i])/speeds[i]))

    total = []
    answer_num = answer[0]
    ans = 1
    for j in range(1,len(answer)):
        if answer[j] <= answer_num:
            ans += 1
        else:
            total.append(ans)
            answer_num = answer[j]
            ans = 1
    total.append(ans)
    return total