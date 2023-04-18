import sys

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if A[a-1] > A[b-1]:
        parent[a] = b
    else:
        parent[b] = a


N, M, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
relationships = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
parent = [_ for _ in range(N+1)]
for relationship in relationships:
    a, b = relationship
    if find(a) != find(b):
        union(a, b)

answer = 0
for i in range(1, N+1):
    if i == parent[i]:
        answer += A[i-1]
print(answer if answer <= k else "Oh no")