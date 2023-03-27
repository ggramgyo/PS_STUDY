# 풀이 참고
def solution(cap, n, deliveries, pickups):
    # 가장 먼 곳부터 탐색위해 reverse
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    d = 0
    p = 0
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        # d, p가 하나라도 양수라면 물류센터에서 다시 와야됨.
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            # cap 값이 음수 -> 수용 가능한 의미
            answer += (n - i) * 2
            # 어차피 물류센터로 돌아가야 하기에 왔던 거리 x2
    return answer