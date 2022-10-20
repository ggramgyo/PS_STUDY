import sys

N, M = map(int, sys.stdin.readline().split())
part = [0]
limit_velocity = []
for _ in range(N):
    d, v = map(int, sys.stdin.readline().split())
    part.append(part[-1] + d)
    limit_velocity.append(v)
reals = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
moving = 0
sector = 0
ans = 0
part.pop(0)
for x in range(M):
    d, v = reals[x]
    # moving -> 1씩 증가시키면서 구간 변경을 탐지
    for y in range(moving, moving+d):
        # 구간 변경 전
        if moving < part[0]:
            if limit_velocity[sector] - v < 0:
                ans = max(ans, v-limit_velocity[sector])
        # 구간 변경 후
        else:
            part.pop(0)
            sector += 1
            if limit_velocity[sector] - v < 0:
                ans = max(ans, v-limit_velocity[sector])
        moving += 1
print(ans)
