import heapq
import sys

tcs = int(sys.stdin.readline())
for tc in range(tcs):
    k = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(files)
    answer = 0
    while True:
        try:
            a, b = heapq.heappop(files), heapq.heappop(files)
            answer += + a + b
            heapq.heappush(files, a+b)
        except IndexError:
            break
    print(answer)
