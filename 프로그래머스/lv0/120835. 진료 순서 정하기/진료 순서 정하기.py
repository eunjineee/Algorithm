def solution(emergency):
    answer = []
    e = emergency[::]
    e.sort(reverse=True)
    for i in emergency:
        answer.append(e.index(i)+1)
    return answer