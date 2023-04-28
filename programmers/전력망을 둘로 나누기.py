from collections import deque, defaultdict
# def solution(n, wires):
#     def find(a):
#         if parent[a] != a:
#             parent[a] = find(parent[a])
#         return parent[a]
#
#     def union(a, b):
#         a = find(a)
#         b = find(b)
#         if a < b:
#             parent[b] = a
#         else:
#             parent[a] = b
#
#     # 하나씩 끊어서 집합으로 따져보자
#     answer = float('inf')
#     qs = deque(wires)
#     l = len(wires)
#     for x in range(l):
#         cnt = defaultdict(int)
#         tmp = qs.popleft()
#         parent = [i for i in range(n+1)]
#         for q in qs:
#             union(q[0], q[1])
#         for p in parent[1:]:
#             cnt[find(p)] += 1
#         cnt = list(cnt.values())
#         answer = min(answer, abs(cnt[0] - cnt[1]))
#         qs.append(tmp)
#
#     return answer

# union-find로 이중 for문으로 완전탐색을 도니 통과는 되지만 시간이 많이 걸린다
# 해결하기 위해 한 노드를 root로 잡고 상위노드 = 하위노드 + 1 이용해 O(n)으로
# abs 최솟값을 구할 수 있다

answer = float('inf')
def solution(n, wires):
    graph = defaultdict(list)
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)
    check = [False] * (n+1)

    def dfs(now_node):
        global answer
        check[now_node] = True
        count = 1
        for next_node in graph[now_node]:
            if not check[next_node]:
                count += dfs(next_node)
        answer = min(answer, abs(n - 2*count))
        return count
    dfs(wires[0][0])

    return answer










