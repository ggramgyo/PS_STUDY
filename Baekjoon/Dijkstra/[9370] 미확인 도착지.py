import heapq
import sys
INF = int(1e9)
from collections import deque


def Dijkstra(s, k):
    heap = [(0, s)]
    check = [INF] * (k + 1)
    check[s] = 0
    while heap:
        cost, start = heapq.heappop(heap)
        if cost > check[start]:
            continue
        for n, v in graph[start]:
            v += cost
            if v < check[n]:
                check[n] = v
                heapq.heappush(heap, (v, n))

    return check


T = int(sys.stdin.readline())
for i in range(T):
    # n: 교차로, m: 도로, t: 목적지 후보
    n, m, t = map(int, sys.stdin.readline().split())
    # s: 예술가의 출발지, g,h 사이의 교차로를 무조건 지나간다.
    s, g, h = map(int, sys.stdin.readline().split())
    # index 고려 n+1
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    endCandidate = [int(sys.stdin.readline()) for _ in range(t)]
    ans = []
    fromStart = Dijkstra(s, n)
    fromG = Dijkstra(g, n)
    fromH = Dijkstra(h, n)
    for c in endCandidate:
        if fromStart[c] == fromStart[g] + fromG[h] + fromH[c] or fromStart[c] == fromStart[h] + fromH[g] + fromG[c]:
            ans.append(c)

    ans.sort()
    print(*ans)