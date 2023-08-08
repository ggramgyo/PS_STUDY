dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
#
# 4 4 2
# 1 2 3 4
# 5 6 7 8
# 9 8 7 6
# 5 4 3 2
def rotate(x, y, direction, temp):
    while direction < 4:
        x = x + dx[direction]
        y = y + dy[direction]


        if 0 <= x < N and 0 <= y < M:
            if not chk[x][y]:
                next_temp = graph[x][y]
                graph[x][y], temp = temp, next_temp
                chk[x][y] = True
            else:
                x -= dx[direction]
                y -= dy[direction]
                direction += 1
        else:
            x -= dx[direction]
            y -= dy[direction]
            direction += 1
    graph[x + dx[direction-1]][y + dy[direction-1]] = temp

N, M, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
for r in range(R):
    chk = [[False] * M for _ in range(N)]
    for start in range(N):
        if start < M:
            if not chk[start][start]:
                chk[start][start] = True
                rotate(start, start, 0, graph[start][start])
for g in graph:
    print(*g)