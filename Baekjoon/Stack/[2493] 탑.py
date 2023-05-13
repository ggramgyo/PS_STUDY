import sys

N = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))[::-1]
stack = []
answer = [0] * N
for i, v in enumerate(tops):
    while stack:
        if stack[-1][1] < v:
            ix, value = stack.pop()
            answer[ix-1] = N-i
        else:
            break
    stack.append((N-i, v))
print(*answer)
