import sys

N = sys.stdin.readline().rstrip()
idx = 0
value = 1
while True:
    i = str(value)
    for j in str(i):
        if N[idx] == j:
            idx += 1
            if idx >= len(N):
                print(i)
                exit()
    value += 1