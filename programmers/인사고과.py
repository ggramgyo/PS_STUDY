def solution(scores):
    answer = 1
    x, y = scores[0]
    # 다중정렬
    scores.sort(key=lambda x:(-x[0], x[1]))
    before = 0
    for i in range(len(scores)):
        nx, ny = scores[i]
        # 둘 다 작으면 완호 탈락
        if nx > x and ny > y:
            return -1
        # 합 등수 계산
        if x+y < nx+ny:
            if before <= y:
                answer += 1
        before = y
    return answer
