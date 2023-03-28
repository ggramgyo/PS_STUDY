from collections import deque


def solution(x, y, n):
    answer = 0
    q = deque()
    q.append((x, 0))
    check = [False] * 1000001
    while q:
        now, t = q.popleft()

        if now > y:
            answer = -1
            continue

        if now == y:
            answer = t
            break
        if not check[now]:
            check[now] = True
            q.append((now*2, t+1))
            q.append((now*3, t+1))
            q.append((now+n, t+1))

    return answer