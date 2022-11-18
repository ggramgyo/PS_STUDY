import heapq

for testcase in range(1, 11):
    N = int(input())
    block = list(map(int, input().split()))
    ma = []
    mi = []
    for i in range(100):
        heapq.heappush(ma, -block[i])
        heapq.heappush(mi, block[i])
    for i in range(N):
        back = heapq.heappop(ma)
        start = heapq.heappop(mi)
        heapq.heappush(ma, back+1)
        heapq.heappush(mi, start+1)
        if -back - start <= 1:
            break

    print("#{} {}".format(testcase, -heapq.heappop(ma)-heapq.heappop(mi)))

