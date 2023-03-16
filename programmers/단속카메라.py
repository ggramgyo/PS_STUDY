def solution(routes):
    answer = 0
    # 빠져나가는 값 기준 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    camera = -30001
    for route in routes:
        start, end = route
        # 들어가는 입구 기준 카메라가 없다면
        if camera < start:
            answer += 1
            # 설치 후 나가는 값 기준으로 리셋
            camera = end
    return answer