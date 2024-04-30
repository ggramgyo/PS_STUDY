import sys
from heapq import heappush, heappop

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

idx = 1
while True:
    cmd = int(sys.stdin.readline())
    if not cmd:
        break

    chk = [[False] * cmd for _ in range(cmd)]
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(cmd)]
    heap = [(graph[0][0], 0, 0)]

    while heap:
        v, x, y = heappop(heap)
        if x == y == cmd - 1:
            print("Problem {}: {}".format(idx, v))
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < cmd and 0 <= ny < cmd and not chk[nx][ny]:
                chk[nx][ny] = True
                heappush(heap, (v + graph[nx][ny], nx, ny))

    idx += 1
