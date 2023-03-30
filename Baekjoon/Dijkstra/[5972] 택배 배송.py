import heapq
import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


heap = []
check = [float('inf') for _ in range(N+1)]
check[1] = 0
heapq.heappush(heap, (0, 1))

while heap:
    cost, start = heapq.heappop(heap)
    for node in graph[start]:
        nt, ct = node
        if ct + check[start] < check[nt]:
            check[nt] = ct + check[start]
            heapq.heappush(heap, (ct, nt))
print(check[-1])
