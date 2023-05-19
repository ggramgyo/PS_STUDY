import sys

N = int(sys.stdin.readline())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
times.sort(key=lambda k: (k[1], k[0]))
answer = 0
end = 0
for i in range(N):
    if end <= times[i][0]:
        answer += 1
        end = times[i][1]
print(answer)
