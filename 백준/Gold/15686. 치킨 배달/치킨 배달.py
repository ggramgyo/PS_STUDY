import itertools
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken = []
house = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 2:
            chicken.append((x, y))
        elif graph[x][y] == 1:
            house.append((x, y))
        else:
            pass


answer = float('inf')
for openChicken in itertools.combinations(chicken, M):
    temp = 0
    for h in house:
        hx, hy = h
        diff = float('inf')
        for oc in openChicken:
            cx, cy = oc
            diff = min(abs(cx - hx) + abs(cy - hy), diff)
        temp += diff
    answer = min(answer, temp)
print(answer)