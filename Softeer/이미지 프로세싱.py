import sys
from collections import deque

rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for _ in range(int(sys.stdin.readline())):
    q = deque()
    n, m, k = map(int, sys.stdin.readline().split())
    n -= 1
    m -= 1
    q.append((n, m))
    target, graph[n][m] = graph[n][m], k
    if target == k:
        continue
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + rx[_]
            ny = y + ry[_]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == target:
                    graph[nx][ny] = k
                    q.append((nx, ny))

for ans in graph:
    print(*ans)