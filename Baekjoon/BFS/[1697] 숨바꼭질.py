import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
check = [False] * 222222
queue = deque()
m_cnt = 0
queue.append((N, 0))

while queue:
    s, cnt = queue.popleft()
    if s == M:
        m_cnt = cnt
        break

    for i in range(3):
        if i == 0 and 1 <= s <= 100000 and not check[s-1]:
            queue.append((s-1, cnt+1))
            check[s-1] = True
        elif i == 1 and 0 <= s <= 100000 and not check[s+1]:
            queue.append((s+1, cnt+1))
            check[s+1] = True
        elif i == 2 and 0 <= s <= 100000 and not check[2*s]:
            queue.append((2*s, cnt+1))
            check[2*s] = True

print(m_cnt)