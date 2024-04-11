import bisect
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = [arr[0]]
result = [0]
for i in range(1, n):
    ix = bisect.bisect_left(res, arr[i])
    if ix == len(res):
        res.append(arr[i])
    else:
        res[ix] = arr[i]
    result.append(ix)

ll = len(res) - 1
ans = []
for i in range(n-1, -1, -1):
    if result[i] == ll:
        ans.append(arr[i])
        ll -= 1
print(len(res))
print(*ans[::-1])
