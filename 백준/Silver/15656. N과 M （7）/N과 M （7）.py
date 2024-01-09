import sys

N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
select = []
def nm7(i):
    if len(select) == M:
        print(*select)
        return
    for j in range(N):
        select.append(nums[j])
        nm7(j)
        select.pop()

for i in range(N):
    select.append(nums[i])
    nm7(i)
    select.pop()
