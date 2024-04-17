import sys
N = int(sys.stdin.readline())
for x in range(N+1):
    print(bin(x)[2:], end='')