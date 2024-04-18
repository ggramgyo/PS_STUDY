import sys
from collections import deque

A, B, N, M = map(int, sys.stdin.readline().split())

q = deque()
q.append((N, 0))
check = [False] * 100001  

while q:
    value, count = q.popleft()
    if value == M:
        print(count)
        break
    if 0 <= value <= 100000 and not check[value]:
        check[value] = True 

        for newValue in [value + A, value - A, value + B, value - B, value * A, value * B, value + 1, value - 1]:
            if 0 <= newValue <= 100000 and not check[newValue]:
                q.append((newValue, count + 1))
