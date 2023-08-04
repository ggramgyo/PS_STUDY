from collections import deque
import sys
q = deque([x for x in range(1, int(sys.stdin.readline()) + 1)])
while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(*q)