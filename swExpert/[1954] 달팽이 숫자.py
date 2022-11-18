def dfs(x, y, i):
    global direction
    if i == N**2 + 1:
        return
    if not arr[x][y]:
        arr[x][y] = i
    nx = x + rx[direction]
    ny = y + ry[direction]
    if 0 <= nx < N and 0 <= ny < N:
        if arr[nx][ny]:
            direction = (direction+1)%4
            nx = x + rx[direction]
            ny = y + ry[direction]
    else:
        direction = (direction + 1) % 4
        nx = x + rx[direction]
        ny = y + ry[direction]

    dfs(nx, ny, i+1)


tc = int(input())
rx = [0, 1, 0, -1]
ry = [1, 0, -1, 0]
for testcase in range(1, tc+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    direction = 0
    dfs(0,0,1)
    print("#{}".format(testcase))
    for r in range(N):
        for c in range(N):
            print("{}".format(arr[r][c]), end=" ")
        print()
