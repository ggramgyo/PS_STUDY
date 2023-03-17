import math


def solution(n, stations, w):
    answer = 0
    # 시간초과 코드 -> 효율성 0
    # check = set()
    # for station in stations:
    #     for i in range(station - w, station + w + 1):
    #         check.add(i)
    # for i in range(1, n + 1):
    #     if not i in check:
    #         answer += 1
    #         for j in range(i, i + 2 * w + 1):
    #             check.add(j)
    start = 1
    l = 2 * w + 1
    # 첫 기지국 왼쪽 남은 공간이 6, 새로 설치한 기지국 영향이 5
    # 최소 2개가 필요 -> (6 / 5) 올림 
    for station in stations:
        left = station - start - w
        if left > 0:
            answer += math.ceil(left / l)

        start = station + w + 1
    
    # 가장 오른쪽에 설치된 기지국까지 탐색 후 나머지 오른쪽 공간도 따져줌
    if n >= start:
        answer += math.ceil((n-start+1) / l)
    return answer


print(math.ceil(0.5))
