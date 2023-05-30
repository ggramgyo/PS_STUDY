# 위상 정렬
# 진입 차수가 없어야 됨, 진출 차수만 있으면 됨. 입력 받을 때 계산
import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
degrees = defaultdict(int)
for _ in range(m):
    li = list(map(int, sys.stdin.readline().split()))
    for i in range(2, li[0]+1):
        edges[li[i]].append(li[i-1])
        edges[li[i-1]].append(li[i])
        degrees[li[i]] += 1
q = deque()
for i in range(1, n+1):
    if not degrees[i]:
        q.append(i)

res = []
check = [False] * (n+1)
while q:
    start = q.popleft()
    if not degrees[start]:
        res.append(start)
    for ne in edges[start]:
        degrees[ne] -= 1
        if not check[ne] and not degrees[ne]:
            q.append(ne)
if len(res) != n:
    print(0)
else:
    for i in res:
        print(i)



