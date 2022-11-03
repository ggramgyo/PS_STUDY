import sys
rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]
N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
check = [[False] * N for _ in range(N)]
stack = []
total = 0
counts = []
for i in range(N):
    for j in range(N):
        if not check[i][j] and graph[i][j] == '1':
            total += 1
            current = 1
            stack.append((i, j))
            check[i][j] = True
            while stack:
                x, y = stack.pop()
                for _ in range(4):
                    nx = rx[_] + x
                    ny = ry[_] + y
                    if 0 <= nx < N and 0 <= ny < N and not check[nx][ny]:
                        if graph[nx][ny] == '1':
                            current += 1
                            check[nx][ny] = True
                            stack.append((nx, ny))
            counts.append(current)
print(total)
for ans in sorted(counts):
    print(ans)