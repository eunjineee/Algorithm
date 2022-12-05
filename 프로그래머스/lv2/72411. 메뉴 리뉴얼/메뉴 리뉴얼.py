from itertools import combinations
def solution(orders, course):
    answer = []
    for cou in range(len(course)):
        ans = {}
        total = []
        for i in orders:
            a = list(combinations(i,course[cou]))
            total += a
        for j in total:
            jjj = []
            for jj in j:
                jjj.append(jj)
            jjj.sort()
            jjj = tuple(jjj)
            if jjj in ans:
                ans[jjj] += 1
            else:
                ans[jjj] = 1
        if len(ans) == 0:
            pass
        else:
            ansmax = max(list(ans.values()))
            if ansmax == 1 or ansmax == 0:
                pass
            else:
                for k in ans:
                    if ans[k] == ansmax:
                        toto = ''
                        for kk in range(len(k)):
                            toto += k[kk]
                        answer.append(toto)
    answer.sort()
    return answer 