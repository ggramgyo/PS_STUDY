def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    for a in A:
        # a가 더 크거나 같다면 점수를 받을 수 없음
        # B arr 중 가장 작은 수랑 교환
        if a >= B[0]:
            continue
        else:
            answer += 1
            del B[0]
    return answer
