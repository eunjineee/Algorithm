def solution(n):
    if n % 6 == 0:
        return n//6
    elif n*2 % 6 == 0:
        return n*2//6
    elif n*3 % 6 == 0:
        return n*3//6
    return n
