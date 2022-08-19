import sys

N, M = map(int, sys.stdin.readline().split())
values = [int(sys.stdin.readline()) for x in range(N)]

dp = [[0] * (M+1) for _ in range(N+1)]
dp[1][1] = values[0]

for x in range(1, N+1):
    dp[x][0] = dp[x-1][0]
    for y in range(1, M+1):
        dp[x][y] = dp[x-1][y-1] + values[x-1]

    for y in range(M + 1):
        dp[x][0] = max(dp[x][0], dp[x-y][y])

print(dp[N][0])