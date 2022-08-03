import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def DFS(idx, rice_cake, yesterday):
    if len(rice_cake) == n:
        for i in rice_cake:
            print(i)
        exit()
    for today in days[idx]:
        if today != yesterday and not ate[idx][today - 1]:
            ate[idx][today - 1] = True
            DFS(idx + 1, rice_cake + [today], today)

n = int(input())
days = [list(map(int, input().split())) for _ in range(n)]
ate = [[False for _ in range(10)] for _ in range(n)]
DFS(0, [], 0)
print(-1)