import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

min_ans = 51
tmp = []
for x in range(1, N+1):
    q = deque()
    check = [False] * (N+1)
    q.append((x, 0))
    check[x] = True
    max_t = 0
    while q:
        start, t = q.popleft()
        max_t = max(t, max_t)
        for i in graph[start]:
            if not check[i]:
                q.append((i, t+1))
                check[i] = True
    tmp.append((max_t, x))
    min_ans = min(min_ans, max_t)
t = 0
ans = []
for x in range(N):
    a, b = tmp[x]
    if a == min_ans:
        t += 1
        ans.append(b)
print(min_ans, t)
print(*ans)
