def solution(money):
    answer = 0
    # 점화식 : dp[i] = max(dp[i-1], dp[i] + dp[i-2])
    # 첫번째와 마지막은 이어져 있음.
    #   1. 첫 번째를 턴 경우 마지막 집은 털 수 없음.
    #   2. 마지막 집을 턴 경우 첫 번째 집은 털 수 없음.
    dpFirst = [0] * len(money)
    dpFirst[0], dpFirst[1] = money[0], money[0]
    for i in range(2, len(money)-1):
        dpFirst[i] = max(dpFirst[i-1], money[i] + dpFirst[i-2])

    dpSecond = [0] * len(money)
    dpSecond[0], dpSecond[1] = 0, money[1]
    for i in range(2, len(money)):
        dpSecond[i] = max(dpSecond[i-1], money[i] + dpSecond[i-2])
    return max(max(dpFirst), max(dpSecond))

solution([1, 2, 3, 1])