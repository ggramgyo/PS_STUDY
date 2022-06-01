import sys
from collections import deque

rx = [0, 1]
ry = [1, 0]
N = int(sys.stdin.readline())
graph = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
check = [[False] * N for _ in range(N)]
q = deque()
q.append((0, 0, graph[0][0]))
check[0][0] = True
results = []
while q:
    x, y, t = q.popleft()
    if x == N -1 and y == N - 1:
        results.append(t)
    for _ in range(2):
        nx = x + rx[_]
        ny = y + ry[_]
        if 0 <= nx < N and 0 <= ny < N:
            if not check[nx][ny]:
                q.append((nx,ny, t+graph[nx][ny]))
ans = []
for result in results:
    a = str(eval(result[:3]))
    for v in result[3:]:
        if not v.isdigit():
            a = str(a) + str(v)
        else:
            a = eval(a+v)
    ans.append(int(a))
print(max(ans), min(ans))