import sys
from collections import defaultdict

T = int(sys.stdin.readline())
for _ in range(T):
    word = sys.stdin.readline().rstrip()
    K = int(sys.stdin.readline())
    e = len(word)

    ch = defaultdict(list)
    for i in range(e):
        if word.count(word[i]) >= K:
            ch[word[i]].append(i)
    three = 10000
    four = 0
    for k, v in ch.items():
        for i in range(len(v)-K+1):
            tmp = v[i+K-1] - v[i] + 1
            three = min(three, tmp)
            four = max(four, tmp)
    if three == 10000 or four == 0:
        print(-1)
    else:
        print(three, four)



