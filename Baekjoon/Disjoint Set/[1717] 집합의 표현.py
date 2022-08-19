import sys
sys.setrecursionlimit(10**9)

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
parent = list(_ for _ in range(N+1))
cmds = [map(int, sys.stdin.readline().split()) for _ in range(M)]

# union-find 알고리즘을 통해 같은 부모를 만나는지 확인

for cmd in cmds:
    s, a, b = cmd
    if s == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')