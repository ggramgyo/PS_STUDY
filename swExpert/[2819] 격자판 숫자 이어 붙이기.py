from collections import deque

N = int(input())

rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]

for testcase in range(1, N+1):
    graph = [list(input().split()) for _ in range(4)]
    q = deque()
    ans = set()
    for x in range(4):
        for y in range(4):
            q.append((x, y, 1, graph[x][y]))
            while q:
                sx, sy, t, now = q.popleft()
                if t == 7:
                    ans.add(now)
                else:
                    for i in range(4):
                        nx = rx[i] + sx
                        ny = ry[i] + sy
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            q.append((nx, ny, t+1, now+graph[nx][ny]))
    print("#{} {}".format(testcase, len(ans)))