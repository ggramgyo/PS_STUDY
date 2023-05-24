import sys

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, sys.stdin.readline().split())
parent = [_ for _ in range(n)]
answer = 0
for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) != find(b):
        union(a, b)
    else:
        answer = i
        break
print(answer)
