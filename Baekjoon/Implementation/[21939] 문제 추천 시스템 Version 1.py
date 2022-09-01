import sys
from collections import defaultdict

level = defaultdict(list)
problem = defaultdict(int)
N = int(sys.stdin.readline())
levels = []
for _ in range(N):
    P, L = map(int, sys.stdin.readline().split())
    levels.append(L)
    if problem[P] != 0:
        level[problem[P]].remove(P)
    problem[P] = L

    level[L].append(P)
M = int(sys.stdin.readline())
for _ in range(M):
    cmd = list(map(str, sys.stdin.readline().rstrip().split()))
    if cmd[0] == 'add':
        levels.append(int(cmd[2]))
        level[int(cmd[2])].append(int(cmd[1]))
        problem[int(cmd[1])] = int(cmd[2])
    elif cmd[0] == 'recommend':
        if cmd[1] == '1':
            print(max(level[max(levels)]))
        else:
            print(min(level[min(levels)]))
    else:
        le = problem[int(cmd[1])]
        level[le].remove(int(cmd[1]))
        levels.remove(le)
