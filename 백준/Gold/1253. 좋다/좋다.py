import sys
#
# def recur(w, k):
#     if len(w) >= N:
#         print(w[N-1])
#         return
#     recur(w+'m'+'o'*k + w, k + 1)
#
#
# N = int(sys.stdin.readline())
# init = 'moo'
# recur(init, 3)

N = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
ans = 0
for i in range(N):
    tmp = nums[:i] + nums[i+1:]
    target = nums[i]
    start, end = 0, N-2
    while start < end:
        t = tmp[start] + tmp[end]
        if t == target:
            ans += 1
            break
        if t < target:
            start += 1
        else:
            end -= 1
print(ans)