def solution(n, k):
    answer = 12000*n
    if k - n//10 <=0:
        return answer
    else:
        answer += 2000*(k-n//10)
    return answer