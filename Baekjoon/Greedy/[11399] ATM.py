import sys

N = int(sys.stdin.readline())
minutes = sorted(list(map(int, sys.stdin.readline().split())))
s = 0
for i in range(1, N+1):
    s += sum(minutes[:i])
print(s)

