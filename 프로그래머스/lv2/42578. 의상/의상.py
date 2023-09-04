def solution(clothes):
    door = {}
    for c in clothes:
        if c[1] not in door:
            door[c[1]] = 1
        else:
            door[c[1]] += 1
            
    answer = list(door.values())     

    ans = 1
    for i in answer:
        ans *= (i+1)
    return ans - 1