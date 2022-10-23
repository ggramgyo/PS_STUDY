import sys
from collections import deque


def topology_sort(N):
    q = deque()
    q.append(1)
    while q:
        now = q.popleft()
        result.append(now)
        for g in graph[now]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)

N, K = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
ans = [0] * (N+1)
indegree = [0] * (N+1)
node_count = [0] * (N+1)
for x in range(1, N+1):
    cmd = list(map(int, sys.stdin.readline().split()))
    node_count[x] = cmd[0]
    if cmd[0]:
        for y in cmd[1:]:
            indegree[y] += 1
            graph[x].append(y)
result = deque()
topology_sort(N)
ans[1] = K
while result:
    start = result.popleft()
    if node_count[start]:
        nc, next_node = node_count[start], graph[start]
        quo, rem = ans[start] // nc, ans[start] % nc
        for i in range(nc):
            ans[next_node[i]] += quo
        for i in range(rem):
            ans[next_node[i]] += 1
    else:
        continue
print(*ans[1:])
