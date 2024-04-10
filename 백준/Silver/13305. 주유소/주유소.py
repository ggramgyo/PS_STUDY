import heapq
import sys

N = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().split()))
gas = list(map(int, sys.stdin.readline().split()))[:-1]
heap = []
for i, v in enumerate(gas):
    heapq.heappush(heap, (v, i))

end = float('inf')
total = 0
charge = set()
while heap:
    price, start = heapq.heappop(heap)
    if start < end:
        charge.add(start)
        end = start

cur = 0
for i in range(N-1):
    if i in charge:
        cur = i
    total += distances[i] * gas[cur]
print(total)