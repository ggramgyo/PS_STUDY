import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lights = list(map(int, sys.stdin.readline().split()))

start = 0
end = N
answer = N
while start <= end:
    mid = (start + end) // 2

    # 첫 번째 위치와 마지막 위치 확인
    if lights[0] - mid > 0 or lights[-1] + mid < N:
        start = mid + 1
        continue

    isLight = True
    for i in range(1, M):
        if lights[i-1] + mid < lights[i] - mid:
            isLight = False
            break

    if isLight:
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1
print(answer)