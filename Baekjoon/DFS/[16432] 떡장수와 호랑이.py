import sys
sys.setrecursionlimit(10**9)

def dfs(t, prev, li):
    if t == N:
        for _ in li:
            print(_)
        exit()
    for now in food[t]:
        if prev != now and not check[t][now]:
            check[t][now] = True
            dfs(t+1, now, li+[now])

N = int(sys.stdin.readline())
food = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(N)]
check = [[False for _ in range(11)] for _ in range(N+1)]

dfs(0, 0, [])
print(-1)