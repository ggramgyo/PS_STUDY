import heapq
import sys
heapPlus = []
heapMinus = []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        heapq.heappush(heapPlus, -num)
    else:
        heapq.heappush(heapMinus, num)
ans = 0

while heapPlus:
    if len(heapPlus) == 1:
        ans += -heapq.heappop(heapPlus)
        break
    a = heapq.heappop(heapPlus)
    b = heapq.heappop(heapPlus)
    if -b == 1:
        ans += -a
        heapq.heappush(heapPlus, b)
    else:
        ans += a * b

while heapMinus:
    if len(heapMinus) == 1:
        ans += heapq.heappop(heapMinus)
        break
    a = heapq.heappop(heapMinus)
    b = heapq.heappop(heapMinus)
    ans += a * b

print(ans)



