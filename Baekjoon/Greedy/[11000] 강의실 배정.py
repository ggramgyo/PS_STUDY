import heapq
import sys
from collections import defaultdict

N = int(sys.stdin.readline())
lec = []
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(lec, (s, e))
room = []
heapq.heappush(room, heapq.heappop(lec)[1])
while lec:
    s, e = heapq.heappop(lec)
    if s < room[0]:
        heapq.heappush(room, e)
    else:
        heapq.heappop(room)
        heapq.heappush(room, e)
print(len(room))