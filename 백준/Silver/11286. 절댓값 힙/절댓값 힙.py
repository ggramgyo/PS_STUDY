import heapq
import sys
heap = []
for _ in range(int(sys.stdin.readline())):
    target = int(sys.stdin.readline())
    if target:
        heapq.heappush(heap, (abs(target), target))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except IndexError:
            print(0)