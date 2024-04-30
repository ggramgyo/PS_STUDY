import sys
from heapq import heappush, heappop
rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]
idx = 1
while True:
    cmd = int(sys.stdin.readline())
    if not cmd: break
    chk = [[False] * cmd for _ in range(cmd)]
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(cmd)]
    heap = [(graph[0][0], 0, 0)]
    while heap:
        v, x, y = heappop(heap)
        if x == cmd-1 and y == cmd-1:
            print("Problem {}: {}".format(idx, v))
            break

        for _ in range(4):
            nx = rx[_]+ x
            ny = ry[_]+ y
            if 0 <= nx < cmd and 0 <= ny < cmd and not chk[nx][ny]:
                chk[nx][ny] = True
                heappush(heap, (graph[nx][ny] + v, nx, ny))


    idx += 1