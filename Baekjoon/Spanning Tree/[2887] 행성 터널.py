import heapq
import sys


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


N = int(sys.stdin.readline())
dots = []
for _ in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    dots.append((_, x, y, z))
parent = [_ for _ in range(N)]
heap = []
for _ in range(1, 4):
    dots.sort(key=lambda k: k[_])
    for i in range(N - 1):
        heapq.heappush(heap, (abs(dots[i][_] - dots[i + 1][_]), dots[i][0], dots[i + 1][0]))

edge = 0
res = 0
while heap:
    if edge == N - 1:
        break
    value, start, end = heapq.heappop(heap)
    if find(start) != find(end):
        union(start, end)
        edge += 1
        res += value
print(res)
