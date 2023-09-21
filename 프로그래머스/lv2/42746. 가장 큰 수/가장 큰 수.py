def solution(numbers):
    answer = ''
    ans_li = []
    for n in numbers:
        ans_li.append(str(n))
    ans_li.sort(key=lambda x:x*3, reverse=True)
    
    for i in ans_li:
        answer += i
    return str(int(answer))