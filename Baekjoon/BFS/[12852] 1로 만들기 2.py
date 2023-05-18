import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([(N, 0, str(N))])
check = [False] * (N+1)

while q:
    n, t, s = q.popleft()
    check[n] = True

    if n == 1:
        print(t)
        print(s)
        break

    if not n % 3 and not check[n // 3]:
        q.append((n // 3, t + 1, s + " " + str(n // 3)))

    if not n % 2 and not check[n // 2]:
        q.append((n // 2, t + 1, s + " " + str(n // 2)))

    if not check[n - 1]:
        q.append((n - 1, t + 1, s + " " + str(n - 1)))