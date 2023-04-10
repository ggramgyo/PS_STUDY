import sys

N, M, K = map(int, sys.stdin.readline().split())
pos = list(map(int, sys.stdin.readline().split()))

start = 0
end = N
res = ""

while start <= end:
    mid = (start + end) // 2
    now = "1"
    cnt = 1
    prev = 0
    for i in range(1, K):
        if cnt == M:
            break
        if pos[i] - pos[prev] >= mid:
            cnt += 1
            now += "1"
            prev = i
        else:
            now += "0"

    while len(now) < K:
        now += "0"

    if cnt != M:
        end = mid - 1
    else:
        start = mid + 1
        res = now

print(res)
