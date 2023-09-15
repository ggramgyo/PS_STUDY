import sys

rx= [0, 0, 1, -1]
ry = [1, -1, 0, 0]


def dfs(x, y, t, v):
    global max_
    if max_ >= (3-t)*max_value + v:
        return
    if t == 3:
        max_ = max(max_, v)
        return
    for _ in range(4):
        nx = x + rx[_]
        ny = y + ry[_]
        if 0 <= nx < N and 0 <= ny < M and not check[nx][ny]:
            if t == 1:
                check[nx][ny] = True
                dfs(x, y, t + 1, v + graph[nx][ny])
                check[nx][ny] = False

            check[nx][ny] = True
            dfs(nx, ny, t+1, v+graph[nx][ny])
            check[nx][ny] = False


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_value = max(map(max, graph))
check = [[False]*M for _ in range(N)]
max_ = 0
for x in range(N):
    for y in range(M):
        check[x][y] = True
        dfs(x, y, 0, graph[x][y])
        check[x][y] = False
print(max_)