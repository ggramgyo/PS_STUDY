import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    d = [0]*(N+1)
    for score in range(N):
        a, b = map(int, sys.stdin.readline().split())
        d[a] = b
    limit = float('inf')
    answer = 0
    for i in range(1, N+1):
        if limit > d[i]:
            limit = d[i]
            answer += 1
    print(answer)