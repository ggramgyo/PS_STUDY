import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# bitmask
INF = int(1e9)
dp = [[None] * (1 << n) for _ in range(n)]
def dfs(route, visited):
    global n
    tmp = []
    # 모든 도시 방문 ex) n = 4 -> 01111, (1,2,3,4) visited
    if visited == (1 << n) - 1:
        if graph[route][0]:
            return graph[route][0]
        else:
            return INF
    # INF 아니라면 이미 값이 있음.
    if dp[route][visited]:
        return dp[route][visited]

    # 모든 도시 팀방
    tmp = INF
    for i in range(1, n):
        # 경로 없다면 pass
        if not graph[route][i]:
            continue
        # 방문 도시라면 pass
        if visited & (1 << i):
            continue
        tmp = min(tmp, dfs(i, visited | (1 << i)) + graph[route][i])
    dp[route][visited] = tmp
    return dp[route][visited]


print(dfs(0, 1))