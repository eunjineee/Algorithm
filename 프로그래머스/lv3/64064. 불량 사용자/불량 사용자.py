from itertools import permutations

def f(user_id, banned_id):
    for j in range(len(user_id)):
        if len(user_id[j]) == len(banned_id[j]):
            for k in range(len(user_id[j])):        
                if banned_id[j][k] != '*' and user_id[j][k] != banned_id[j][k]:
                    return False
        else:
            return False
    return True


def solution(user_id, banned_id):
    answer = []
    for i in permutations(user_id, len(banned_id)):
        if f(i, banned_id):
            i = set(i)
            if i not in answer:
                answer.append(i)
    return len(answer)