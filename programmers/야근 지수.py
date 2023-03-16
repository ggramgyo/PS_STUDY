import heapq

def solution(n, works):
    # n 값이 더 크다면 모든 일 처리가 됨
    if sum(works) <= n:
        return 0
    start = 0
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
    # 힙 정렬로 최댓값 -1
    while start != n:
        working = heapq.heappop(heap) + 1
        heapq.heappush(heap, working)
        start += 1
    answer = 0
    for h in heap:
        answer += (h ** 2)
    return answer
