from collections import deque
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    A = deque(A)
    B = deque(B)
    # print(A,B)
    while len(A) != 0:
        a = A.popleft()
        b = B.popleft()
        if a <b:
            answer += 1
        else:
            B.appendleft(b)
    return answer