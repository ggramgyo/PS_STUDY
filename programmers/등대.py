from collections import defaultdict, deque


def solution(n, lighthouse):
    answer = 0
    indegree = defaultdict(int)
    graph = defaultdict(set)
    for lh in lighthouse:
        a, b = lh
        indegree[a] += 1
        indegree[b] += 1
        graph[a].add(b)
        graph[b].add(a)
    q = set()
    check = [False] * (n+1)
    for nc in indegree.items():
        n, cnt = nc
        if cnt == 1:
            q.add(n)
    while q:
        now = q.pop()
        if indegree[now] != 1:
            continue
        for gh in graph[now]:
            indegree[gh] -= 1
            if not check[now] and not check[gh]:
                answer += 1
                check[gh] = True
            if indegree[gh] == 1:
                q.add(gh)

    return answer