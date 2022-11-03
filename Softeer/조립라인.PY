import sys

N = int(sys.stdin.readline())
A, B = [], []
for i in range(N-1):
    a, b, ab, ba = map(int, sys.stdin.readline().split())
    A.append((a, ab))
    B.append((b, ba))
last = list(map(int, sys.stdin.readline().split()))
A.append((last[0], -1))
B.append((last[1], -1))
dpA = [0] * N
dpB = [0] * N
dpA[0], dpB[0] = A[0][0], B[0][0]
for i in range(1, N):
    # 1. A 에서 B로 이동
    # 2. A 에서 A로 이동
    dpA[i] = min(dpA[i-1] + A[i][0], dpB[i-1] + B[i-1][1] + A[i][0])
    dpB[i] = min(dpB[i-1] + B[i][0], dpA[i-1] + A[i-1][1] + B[i][0])
print(min(dpA[N-1], dpB[N-1]))