from itertools import permutations

def solution(k, dungeons):
    answer = 0
    len_dungeons = len(dungeons)
    for permu in permutations(dungeons, len_dungeons):  # 순열로 경우를 만들어줌
        temp_k = k  # k는 그대로 보존하기 위해 temp_k를 k로 초기화 하고 사용
        count = 0  # 던전 수
        for p in permu:
            if temp_k >= p[0]:  # 최소 필요 피로도가 있는지 확인
                temp_k -= p[1]  # 소모 피로도 빼주기
                count += 1  # 던전 수 업데이트
        answer = max(answer, count)  # 최대 던전 탐험 수 업데이트
    return answer