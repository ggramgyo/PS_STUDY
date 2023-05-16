import sys
from collections import defaultdict


def bell(start):
    check[start] = 0
    for _ in range(N):
        for i in range(1, N + 1):
            # edge
            for gph in graph[i]:
                end, value = gph
                if check[end] > check[i] + value:
                    check[end] = check[i] + value
                    if _ == N - 1:
                        return True
    return False


for tc in range(int(sys.stdin.readline())):
    N, M, W = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        graph[S].append((E, T))
        graph[E].append((S, T))

    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        graph[S].append((E, -T))
    check = [int(1e9)] * (N + 1)
    if bell(1):
        print('YES')
    else:
        print('NO')
