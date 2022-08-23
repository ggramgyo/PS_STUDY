import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)


def dfs(current):
    global totalFileCount
    for nt in files[current]:
        if not check[nt[0]]:
            # 1 : 폴더
            # 0 : 파일
            if nt[1] == 1:
                check[nt[0]] = True
                dfs(nt[0])
            else:
                totalFileCount += 1
                totalFileKinds.add(nt[0])


N, M = map(int, sys.stdin.readline().split())
tree = defaultdict(list)
files = defaultdict(list)
for _ in range(N+M):
    Folder, currentThing, isFile = map(str, sys.stdin.readline().split())
    files[Folder].append((currentThing, int(isFile)))

queryCnt = int(sys.stdin.readline())
for _ in range(queryCnt):
    query = sys.stdin.readline().rstrip().split('/')[-1]
    check = defaultdict(bool)
    totalFileKinds = set()
    totalFileCount = 0
    dfs(query)
    print(len(totalFileKinds), totalFileCount)
