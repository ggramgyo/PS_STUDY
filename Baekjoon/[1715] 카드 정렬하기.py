import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))
ans = 0
while heap:
    if len(heap) == 1:
        print(ans)
        break
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, a+b)