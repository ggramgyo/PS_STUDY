import sys


def one():
    graph.reverse()


def two():
    for g in graph:
        g.reverse()


def three():
    global N, M

    new_graph = []
    for j in range(M):
        li = []
        for i in range(N - 1, -1, -1):
            li.append(graph[i][j])
        new_graph.append(li)
    N, M = M, N
    return new_graph


def four():
    global N, M
    new_graph = []
    for j in range(M - 1, -1, -1):
        li = []
        for i in range(N):
            li.append(graph[i][j])
        new_graph.append(li)
    N, M = M, N
    return new_graph


def five():
    global N, M
    temp = []
    for i in range(N // 2):
        li = []
        for j in range(M // 2):
            li.append(graph[i][j])
        temp.append(li)
    for i in range(N // 2, N):
        for j in range(M // 2):
            graph[i - N // 2][j] = graph[i][j]
    for i in range(N // 2, N):
        for j in range(M // 2, M):
            graph[i][j - M // 2] = graph[i][j]
    for i in range(N // 2):
        for j in range(M // 2, M):
            graph[i + N // 2][j] = graph[i][j]
    for i in range(N // 2):
        for j in range(M // 2, M):
            graph[i][j] = temp[i - N // 2][j - M // 2]


def six():
    global N, M
    temp = []
    for i in range(N // 2):
        li = []
        for j in range(M // 2):
            li.append(graph[i][j])
        temp.append(li)
    for i in range(N // 2):
        for j in range(M // 2, M):
            graph[i][j-M//2] = graph[i][j]
    for i in range(N // 2, N):
        for j in range(M // 2, M):
            graph[i-N//2][j] = graph[i][j]
    for i in range(N // 2, N):
        for j in range(M // 2):
            graph[i][j+M//2] = graph[i][j]
    for i in range(N // 2, N):
        for j in range(M // 2):
            graph[i][j] = temp[i - N // 2][j]


N, M, R = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
query = list(map(int, sys.stdin.readline().split()))
for q in query:
    if q == 1:
        one()
    elif q == 2:
        two()
    elif q == 3:
        graph = three()
    elif q == 4:
        graph = four()
    elif q == 5:
        five()
    else:
        six()

for g in graph:
    print(*g)
