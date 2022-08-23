import sys
from collections import defaultdict

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
files = defaultdict(set)
for _ in range(N+M):
    Folder, currentThing, isFile = map(str, sys.stdin.readline().split())
    files[Folder].add((currentThing, int(isFile)))
# K: 옮기는 횟수
K = int(sys.stdin.readline())
cmds = []
for _ in range(K):
    fr, to = map(str, sys.stdin.readline().split())
    cmds.append((fr.split('/')[-1], to.split('/')[-1]))
for cmd in cmds:
    fr, to = cmd
    for file in list(files[fr]):
        files[to].add(file)
        files[fr].remove(file)

queryCnt = int(sys.stdin.readline())
for _ in range(queryCnt):
    query = sys.stdin.readline().rstrip().split('/')[-1]
    check = defaultdict(bool)
    totalFileKinds = set()
    totalFileCount = 0
    dfs(query)
    print(len(totalFileKinds), totalFileCount)
