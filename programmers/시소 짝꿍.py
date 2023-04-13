from collections import defaultdict


def solution(weights):
    weight_cnt = defaultdict(int)
    for w in weights:
        weight_cnt[w] += 1
    answer = 0
    for w in list(weight_cnt):
        # 중복 값은 별도 처리
        if weight_cnt[w] > 1:
            answer += weight_cnt[w] * (weight_cnt[w] - 1) // 2
        for v in [3/2, 4/3, 4/2]:
            weight_expect = w * v
            if weight_cnt[int(weight_expect)] > 0:
                answer += weight_cnt[weight_expect] * weight_cnt[w]

    return answer
