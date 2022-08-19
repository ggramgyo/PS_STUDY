import sys
from collections import defaultdict

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


N, M = map(int, sys.stdin.readline().split())
schools = list(map(str, sys.stdin.readline().rstrip().split()))
parent = list(_ for _ in range(N+1))
d = []
for _ in range(M):
    s, e, v = map(int, sys.stdin.readline().split())
    # 조건 1번 처리
    if schools[s-1] != schools[e-1]:
        d.append([s, e, v])
d.sort(key=lambda x: x[2])

edge = 0
cost = 0
for i in d:
    s, e, v = i
    if edge == N-1:
        break
    if find(s) != find(e):
        union(s, e)
        cost += v
        edge += 1

print(cost if edge == N-1 else -1)