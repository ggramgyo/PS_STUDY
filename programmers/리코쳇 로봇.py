from collections import deque

rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]

def solution(board):
    answer = 0
    height = len(board)
    width = len(board[0])
    q = deque()
    for x in range(height):
        for y in range(width):
            if board[x][y] == 'R':
                q.append((x, y, 0))
    check = [[False] * width for _ in range(height)]
    check[q[0][0]][q[0][1]] = True
    while q:
        sx, sy, cnt = q.popleft()
        if board[sx][sy] == 'G':
            break
        for i in range(4):
            nx, ny = sx, sy
            while True:
                nx = nx + rx[i]
                ny = ny + ry[i]
                # 경계선에 닿거나 장애물을 만났을 땐 멈춰서 break
                if 0 > nx or nx >= height or 0 > ny or ny >= width or board[nx][ny] == 'D':
                    nx -= rx[i]
                    ny -= ry[i]
                    break
            if not check[nx][ny]:
                q.append((nx, ny, cnt+1))
                check[nx][ny] = True
    return answer if answer else -1