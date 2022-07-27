import sys


def backTracking(d, k):
    if d == 0:
        res.add(k)
        return
    for x in range(26):
        if alpha[x] >= 1:
            alpha[x] -= 1
            backTracking(d-1, k + chr(x + 97))
            alpha[x] += 1


for _ in range(int(sys.stdin.readline())):
    w = list(map(str, sys.stdin.readline().rstrip()))
    res = set()
    l = len(w)
    alpha = [0 for _ in range(26)]
    for i in w:
        alpha[ord(i)-97] += 1
    backTracking(l, '')
    for a in sorted(list(res)):
        print(a)
