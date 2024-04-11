import sys

N = int(sys.stdin.readline())
local = sorted(list(map(int, sys.stdin.readline().split())))
limit = int(sys.stdin.readline())

if sum(local) <= limit:
    print(max(local))
else:
    start = 0
    end = max(local)

    while start <= end:
        mid = (start + end) // 2
        total = 0

        for budget in local:
            if budget > mid:
                total += mid
            else:
                total += budget

        if total <= limit:
            start = mid + 1
        else:
            end = mid - 1

    print(end)