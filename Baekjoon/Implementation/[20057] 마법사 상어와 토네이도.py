import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 바라보는 방향 ix : 왼쪽, 아래, 오른쪽, 위
ix = {
    (0, -1): 0,
    (1, 0): 1,
    (0, 1): 2,
    (-1, 0): 3
}
# 위 아래,왼,오 위위 아래아래, 앞앞, 뒤뒤, 오른 대각 위 아래, 왼 대각 위 아래
value = {
    (-1, 0): [7, 0, 7, 0],
    (1, 0): [7, 0, 7, 0],
    (0, -1): [0, 7, 0, 7],
    (0, 1): [0, 7, 0, 7],
    (-2, 0): [2, 0, 2, 5],
    (2, 0): [2, 5, 2, 0],
    (0, -2): [5, 2, 0, 2],
    (0, 2): [0, 2, 5, 2],
    (-1, 1): [1, 1, 10, 10],
    (1, 1): [1, 10, 10, 1],
    (-1, -1): [10, 1, 1, 10],
    (1, -1): [10, 10, 1, 1]
}

x, y = N // 2, N // 2
dx, dy = 0, -1
answer = 0
for _ in range(N ** 2):
    # 토네이도 다음 이동경로에 모래가 있는 경우
    nx, ny = x + dx, y + dy
    if graph[nx][ny]:
        # 토네이도 방향
        dir_index = ix[(dx, dy)]
        tmp = 0
        for k, v in value.items():
            tx, ty = k
            ttx, tty = tx + nx, ty + ny
            percentage = v[dir_index]
            move_sand = int(graph[nx][ny] * 0.01 * percentage)
            tmp += move_sand
            if 0 <= ttx < N and 0 <= tty < N:
                graph[ttx][tty] += move_sand
            else:
                answer += move_sand

        if tmp != graph[nx][ny]:
            if 0 <= nx + dx < N and 0 <= ny + dy < N:
                graph[nx + dx][ny + dy] += (graph[nx][ny] - tmp)
            else:
                answer += (graph[nx][ny] - tmp)
        graph[nx][ny] = 0
    # 방향 전환 조건
    if (N - ny - 1 == nx) or (x == y and nx > ny) or (N - nx - 1 == ny) or (nx == ny and x > y):
        dx, dy = -dy, dx
    x = nx
    y = ny

print(answer)
