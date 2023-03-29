def solution(k, d):
    answer = 0
    # x축 기준으로 따져줌 원점을 포함하기 위해 + 1
    for i in range(0, d + 1, k):
        answer += (d ** 2 - (i) ** 2) ** (1 / 2) // k + 1

    return answer