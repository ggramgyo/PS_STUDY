import heapq
import sys

N = int(sys.stdin.readline())
lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lectures.sort(key=lambda x: (x[1], -x[2]))

answer = 0
heap = []
for lecture in lectures:
    _, start, end = lecture
    while heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)
    answer = max(answer, len(heap))

print(answer)
