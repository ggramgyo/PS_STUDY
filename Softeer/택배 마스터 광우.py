import sys
from itertools import permutations

N, M, K = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
ans = float('inf')
for x in permutations(w, len(w)):
    k = 0
    t = 0
    ix = 0
    tmp = 0
    while True:
        t += x[ix]
        if tmp > ans:
            break
        if t > M:
            k += 1
            tmp += (t - x[ix])
            t = x[ix]
        if k >= K:
            ans = min(ans, tmp)
            break
        ix = (ix+1) % len(w)
print(ans)