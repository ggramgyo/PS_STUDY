import sys

N = int(sys.stdin.readline())
graph = [[False] * 100 for _ in range(100)]
answer = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            if not graph[i][j]:
                graph[i][j] = True
                answer += 1
print(answer)