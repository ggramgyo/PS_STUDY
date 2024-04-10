import sys
from copy import deepcopy

N = int(sys.stdin.readline())
start = list(map(int, list(sys.stdin.readline().strip())))
end = list(map(int, list(sys.stdin.readline().strip())))


def flip(arr, idx):
    global N
    for i in range(idx - 1, idx + 2):
        if 0 <= i < N:
            arr[i] = 1 - arr[i]


def check_arr(s, e):
    count = 0
    temp = deepcopy(s)
    for i in range(1, N):
        if temp[i - 1] != e[i - 1]:
            flip(temp, i)
            count += 1
    if temp == e:
        return count
    else:
        return float('inf')


c1 = check_arr(start, end)
start[0] = 1 - start[0]
start[1] = 1 - start[1]
c2 = check_arr(start, end) + 1

print(-1 if min(c1, c2) == float('inf') else min(c1, c2))
