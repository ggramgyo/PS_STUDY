from collections import deque
# 머리 아프다
# https://velog.io/@tjdud0123/%EB%B8%94%EB%A1%9D-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python
# 참고 없이는 못 풀겠다 ;
rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]


def ttt(nx, ny, n):
    a, b = nx
    c, d = ny
    if 0 <= a <= n and 0 <= b <= n and 0 <= c <= n and 0 <= d <= n:
        return True
    return False

def solution(board):
    answer = 0
    n = len(board) - 1
    q = deque([((1, 1), (1, 2), 0)])
    check = set(((0, 0), (0, 1)))
    while q:
        cx, cy, cnt = q.popleft()
        if cx == (n , n ) or cy == (n , n ):
            return cnt

            # 가능한 범위 추리기
        nt = []
        # 평행 이동
        for i in range(4):
            nx = (rx[i] + cx[0], ry[i] + cx[1])
            ny = (rx[i] + cy[0], ry[i] + cy[1])
            if ttt(nx, ny, n):
                if not board[nx[0]][nx[1]] and not board[ny[0]][ny[1]]:
                    nt.append((nx, ny))

        # 회전 이동
        # 가로
        if cx[0] == cy[0]:
            # 위 체크, 아래 체크
            for i in [-1, 1]:
                nx = (cx[0] + i, cx[1])
                ny = (cy[0] + i, cy[1])
                if ttt(nx, ny, n):
                    if not board[nx[0]][nx[1]] and not board[ny[0]][ny[1]]:
                        nt.append((cx, nx))
                        nt.append((ny, cy))
        else:
            # 왼쪽 체크, 오른쪽 체크
            for i in [-1, 1]:
                nx = (cx[0], cx[1] + i)
                ny = (cy[0], cy[1] + i)
                if ttt(nx, ny, n):
                    if not board[nx[0]][nx[1]] and not board[ny[0]][ny[1]]:
                        nt.append((nx, cx))
                        nt.append((ny, cy))
        for n_t in nt:
            if n_t not in check:
                q.append((*n_t, cnt+1))
                check.add(n_t)

