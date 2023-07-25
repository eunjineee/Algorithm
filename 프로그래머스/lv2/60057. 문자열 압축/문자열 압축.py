def solution(s):
    answer = 1000000000000
    if len(s) == 1:
        answer = 1
    for i in range(1,len(s)):
        total = len(s)
        num = 2*i
        word = s[:i]
        repeat = 0
        while num <= len(s):
            # print('i',s[num-i:num])
            if word == s[num-i:num]:
                repeat += 1
            else:
                word = s[num-i:num]
                if repeat != 0:
                    if repeat > 8:
                        total -= (repeat*i-2)
                    else:
                        total -= (repeat*i-1)
                    repeat = 0
            num += i
        if repeat > 0:
            if repeat > 8:
                total -= (repeat*i-2)
            else:
                total -= (repeat*i-1)
        
        if  answer > total:
            answer = total
    return answer
