from itertools import combinations_with_replacement

def solution(n, info):
    lion_nums = list(combinations_with_replacement(range(0,11),n))
    maxcha = float("-inf")
    answer = [-1]
    for lion_num in lion_nums:
        lion = [0]*11
        for score in lion_num:
            lion[10 - score] += 1
        
        apeach_score = 0
        lion_score = 0
        for i in range(11):
            if info[i] == lion[i] == 0:
                continue
            elif info[i] >= lion[i]:
                apeach_score += (10-i)
            else:
                lion_score += (10-i)

        if lion_score > apeach_score:
            chai = lion_score - apeach_score
            if chai > maxcha:
                maxcha = chai
                answer = lion

    return answer