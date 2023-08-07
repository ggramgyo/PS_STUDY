import sys
N = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [0] * N
for ix in range(N-1, -1, -1):
    target = tops[ix]
    if not stack or stack[-1][0] > target:
        stack.append((target, ix))
    else:
        while stack and stack[-1][0] < target:
            temp = stack.pop()
            answer[temp[1]] = ix+1
        stack.append((target, ix))
print(*answer)