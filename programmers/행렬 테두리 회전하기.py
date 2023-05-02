import heapq
def rotate(graph, query):
    heap = []
    sx, sy, ex, ey = query
    r, d, l, u = graph[sx-1][sy-1], graph[sx-1][ey-1], graph[ex-1][ey-1], graph[ex-1][sy-1]
    heapq.heappush(heap, r)
    heapq.heappush(heap, d)
    heapq.heappush(heap, l)
    heapq.heappush(heap, u)
    # right
    for i in range(ey-1, sy-1, -1):
        heapq.heappush(heap, graph[sx-1][i-1])
        graph[sx-1][i] = graph[sx-1][i-1]
    # down
    for i in range(ex-1, sx-1, -1):
        heapq.heappush(heap, graph[i-1][ey-1])
        graph[i][ey-1] = graph[i-1][ey-1]
    graph[sx][ey-1] = d
    # left
    for i in range(sy-1, ey-1):
        heapq.heappush(heap, graph[ex-1][i+1])
        graph[ex-1][i] = graph[ex-1][i+1]
    graph[ex-1][ey-2] = l
    #up
    for i in range(sx-1, ex-1):
        heapq.heappush(heap, graph[i+1][sy-1])
        graph[i][sy-1] = graph[i+1][sy-1]
    graph[ex-2][sy-1] = u
    return heapq.heappop(heap)


def solution(rows, columns, queries):
    answer = []
    graph = [[y for y in range(x*columns+1, (x+1)*columns+1)] for x in range(rows)]
    for query in queries:
        answer.append(rotate(graph, query))
    return answer

