import heapq
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
pos = sorted(list(map(int, sys.stdin.readline().split())))
heap = []
for i in range(N-1):
    heapq.heappush(heap, pos[i+1] - pos[i])
res = 0
for _ in range(N-K):
    res += heapq.heappop(heap)
print(res)