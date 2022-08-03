import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

s = 1
e = 2 * (10 ** 9)
while s <= e:
    mid = (s + e) // 2
    t = 0
    for tree in trees:
        if mid < tree:
            t += (tree - mid)
    if t >= M:
        s = mid + 1
    else:
        e = mid - 1
print(e)