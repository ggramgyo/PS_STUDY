import sys
sys.setrecursionlimit(10**5)
# dfs 재귀로 돌면 무조건 넣자

rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]


def solution(maps):
    global landSize
    answer = []
    height = len(maps)
    width = len(maps[0])
    check = [[False] * width for _ in range(height)]

    def dfs(x, y):
        global landSize
        for i in range(4):
            nx = x + rx[i]
            ny = y + ry[i]
            # 경계면 and 방문 X
            if 0 <= nx < height and 0 <= ny < width and not check[nx][ny]:
                # 바다 X
                if maps[nx][ny] != 'X':
                    check[nx][ny] = True
                    landSize += int(maps[nx][ny])
                    dfs(nx, ny)

    for x in range(height):
        for y in range(width):
            if not check[x][y]:
                check[x][y] = True
                landSize = 0
                if maps[x][y] != 'X':
                    landSize += int(maps[x][y])
                    dfs(x, y)
                    answer.append(landSize)
                    answer.sort()
    return answer if answer else [-1]
