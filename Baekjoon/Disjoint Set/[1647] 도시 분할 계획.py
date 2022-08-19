import sys


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


N, E = map(int,sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for x in range(E)]
graph.sort(key=lambda x: x[2])
parent = list(_ for _ in range(N+1))

edge = 0
cost = 0
for x in graph:
    if edge == N-2:
        break
    u, v, w = x
    if find(u) != find(v):
        union(u, v)
        cost += w
        edge += 1

print(cost)