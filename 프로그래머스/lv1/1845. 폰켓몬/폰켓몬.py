def solution(nums):
    answer = 0
    cnt = len(nums)/2
    answer = len(set(nums))
    if answer < cnt:
        return answer
    else:
        return cnt