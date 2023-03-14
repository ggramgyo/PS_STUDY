from collections import defaultdict, deque

# 모든 source 정점에서 시작해서 BFS 돌릴 시 시간초과
# 목적지부터 거꾸로 BFS 돌려 거리 저장 후 탐색
def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)
    q = deque()
    q.append(destination)
    check = [0] * (n+1)
    while q:
        start = q.popleft()

        for next_node in graph[start]:
            if not check[next_node]:
                check[next_node] = check[start] + 1
                q.append(next_node)
    for source in sources:
        if source == destination:
            answer.append(0)
        else:
            answer.append(check[source]) if check[source] else answer.append(-1)

    return answer
