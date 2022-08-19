import sys
from collections import deque

# union find 알고리즘을 사용하면 쉬운 문제
# 처음에 알고리즘이 기억 나질 않아
# route에서 다음 경로까지 bfs 탐색 -> 시간초과 고려(연결 안된 경우) 40000 초과 시 NO (N <= 200)
# 비효율적이다. union-find 이용해서 다시 풀어봐야겠다.

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
route = list(map(int, sys.stdin.readline().split()))
go = True
for k in range(M-1):
    if go:
        queue = deque()
        queue.append(route[k]-1)
        t = 0
        while queue and t < 40000:
            start = queue.popleft()
            if start == route[k+1]-1:
                break
            for i in range(N):
                if graph[start][i]:
                    queue.append(i)
            t += 1
        else:
            print('NO')
            exit()
print('YES')