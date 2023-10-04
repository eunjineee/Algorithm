def solution(citations):
    citations.sort()
    c = len(citations)
    for i in range(c):
        if c-i <= citations[i]:
            return c-i
    return 0
    