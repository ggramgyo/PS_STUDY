from collections import deque

rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]
def solution(maps):
    answer = 0
    q = deque()
    height = len(maps)
    width = len(maps[0])
    fx, fy = 0, 0
    for x in range(height):
        for y in range(width):
            if maps[x][y] == 'S':
                q.append((x, y))
            if maps[x][y] == 'E':
                fx, fy = x, y
    check = [[0] * width for _ in range(height)]
    lever_check = False
    while q:
        x, y = q.popleft()
        if not lever_check and maps[x][y] == 'L':
            # 레버 찾은 뒤 q, check 초기화 후 다시 탐색 진행
            # lever_check : 레버를 찾지 않고 S -> E 간 경우 값 RETURN 방지
            lever_check = True
            tmp = check[x][y]
            check = [[0] * width for _ in range(height)]
            check[x][y] = tmp
            q = deque()
        for _ in range(4):
            nx = x + rx[_]
            ny = y + ry[_]
            if 0 <= nx < height and 0 <= ny < width:
                if maps[nx][ny] != 'X' and not check[nx][ny]:
                    check[nx][ny] = check[x][y] + 1
                    q.append((nx, ny))
    return check[fx][fy] if check[fx][fy] and lever_check else -1
