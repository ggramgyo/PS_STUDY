import sys

P, N = map(int, sys.stdin.readline().split())
virus = list(map(int, sys.stdin.readline().split()))
dp = [0] * (N+1)
for x in range(1, N+1):
    dp[x] = (dp[x-1] * P + virus[x-1])%1000000007
print(dp[-1])