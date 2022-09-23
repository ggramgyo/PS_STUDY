import sys
import heapq
from collections import defaultdict

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
heap = []
num_index = defaultdict(int)
for ix in range(N):
    num_index[nums[ix]] = ix
    heapq.heappush(heap, nums[ix])
count = 0

for ix in range(N):
    tmp = heapq.heappop(heap)
    if nums[ix] != tmp:
        tix = num_index[tmp]
        num_index[nums[ix]] = tix
        nums[ix], nums[tix] = nums[tix], nums[ix]
        count += 1
print(count)