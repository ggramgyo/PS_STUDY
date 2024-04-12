import sys

N, M = map(int, input().split())
fishcake = [list(sys.stdin.readline().strip()) for _ in range(N)]
for f in fishcake:
    print("".join(f[::-1]))