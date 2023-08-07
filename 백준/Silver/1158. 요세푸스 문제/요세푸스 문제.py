import sys
n, m = map(int, sys.stdin.readline().split())
arr = [str(x) for x in range(1, n+1)]
res = []
index = m - 1
for _ in range(n):
    res.append(arr.pop(index))
    if arr:
        index = (index + m - 1) % len(arr)
print('<' +", ".join(res)+ '>')