import sys

N = int(sys.stdin.readline())
dots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dots.sort(key=lambda k: k[0])
x = dots[N // 2][0]
dots.sort(key=lambda k: k[1])
y = dots[N // 2][1]
ans = 0
for i, j in dots:
    ans += abs(i - x) + abs(j - y)
print(ans)