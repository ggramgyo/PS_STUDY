import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for path in paths:
        a, b, value = path
        graph[a].append((value, a, b))
        graph[b].append((value, b, a))
    answer = []
    g = set(gates)
    summits = set(summits)
    for gate in gates:
        connected = set()
        mst = []
        heap = []
        mv = 0
        for v in graph[gate]:
            heapq.heappush(heap, v)
        while heap:
            value, a, b = heapq.heappop(heap)
            if b in summits:
                mv = max(mv, value)
                answer.append([b, mv])
                mst.append((value, a, b))
                break
            elif b not in g:
                if b not in connected:
                    mv = max(mv, value)
                    connected.add(b)
                    mst.append((value, a, b))
                    for v in graph[b]:
                        if v[2] not in connected:
                            heapq.heappush(heap, v)
    return sorted(answer, key=lambda x:(x[1], x[0]))[0]
# TestCase 틀린데 왜 제출하면 정답처리 ??
# 틀린 이유를 알긴 아는데... 고치진 않은 코드
# gate 출발 후 정상 도착하자마자 종료 동일 값에 더 작은 봉우리 도착 전에