def solution(numbers, target):
    answer = 0
    def f(num, total):
        if num == len(numbers):
            if total == target:
                nonlocal answer
                answer += 1  
        elif num < len(numbers):
            dd = ['+' , '-']
            for d in dd:
                if d == '-':
                    total -= numbers[num]
                    f(num+1,total)
                    total += numbers[num]
                else:
                    total += numbers[num]
                    f(num+1,total)
                    total -= numbers[num]
    f(0,0)
    return answer