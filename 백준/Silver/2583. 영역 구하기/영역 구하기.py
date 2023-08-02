import sys
sys.setrecursionlimit(10**9)

def dfs(x, y):
    global N, M, tmp
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < N and 0 <= ny < M:
            if not chk[ny][nx] and not graph[ny][nx]:
                chk[ny][nx] = True
                tmp += 1
                dfs(nx, ny)


M, N, K = map(int, sys.stdin.readline().split())
dots = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
graph = [[False] * N for _ in range(M)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for dot in dots:
    sx, sy, ex, ey = dot
    for y in range(sy, ey):
        for x in range(sx, ex):
            graph[y][x] = True

answer = 0
count = []
chk = [[False] * N for _ in range(M)]
for y in range(M):
    for x in range(N):
        tmp = 1
        if not chk[y][x] and not graph[y][x]:
            chk[y][x] = True
            answer += 1
            dfs(x, y)
            count.append(tmp)

print(answer)
print(*sorted(count))
