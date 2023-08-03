def solution(people, limit):
    answer = 0
    people = sorted(people)
    s = 0
    e = len(people)-1
    while s < e:
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
        else:
            e -= 1
        answer += 1
        if s == e:
            answer += 1
            break
    return answer