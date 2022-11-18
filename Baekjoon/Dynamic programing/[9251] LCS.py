import sys

stringA = ['-'] + list(sys.stdin.readline().rstrip())
stringB = ['-'] + list(sys.stdin.readline().rstrip())
la = len(stringA)
lb = len(stringB)
dp = [[0] * la for _ in range(lb)]
for x in range(lb):
    for y in range(la):
        if x == 0 or y == 0:
            pass
        elif stringA[y] == stringB[x]:
            dp[x][y] = dp[x-1][y-1] + 1
        else:
            dp[x][y] = max(dp[x-1][y], dp[x][y-1])
print(dp[-1][-1])