import sys
rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]

# 백트래킹을 이용해서 풀면 시간초과
# 이미 탐색한 경로라면 DP 이용해서 시간 단축
# DP 값이 1 이상이라면 이전에 그 만큼 방문한 경로 값이 있으므로 그 값을 반환

def dfs(x, y):
    global ans
    if x == N-1 and y == M-1:
        return 1
    if check[x][y] != -1:
        return check[x][y]
    check[x][y] = 0
    for _ in range(4):
        nx = rx[_] + x
        ny = ry[_] + y
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] < graph[x][y]:
                check[x][y] += dfs(nx, ny)
    return check[x][y]

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = [[-1] * M for _ in range(N)]
print(dfs(0, 0))