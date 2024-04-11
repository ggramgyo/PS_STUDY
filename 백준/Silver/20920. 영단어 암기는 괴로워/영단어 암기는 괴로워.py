import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
priority = defaultdict(tuple)
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    value = priority[word]
    if value:
        freq, long = value
        priority[word] = (freq + 1, long)
    else:
        priority[word] = (1, len(word))

answer = sorted(priority.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))
for word, value in answer:
    if len(word) >= M:
        print(word)
