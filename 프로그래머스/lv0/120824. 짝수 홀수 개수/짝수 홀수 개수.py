def solution(num_list):
    ans1,ans2 = 0, 0
    for i in num_list:
        if i % 2 == 1:
            ans2 += 1
        else:
            ans1 += 1
    answer = [ans1,ans2]

    return answer