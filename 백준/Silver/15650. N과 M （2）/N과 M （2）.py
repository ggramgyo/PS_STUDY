import sys
from itertools import permutations
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
items = [x for x in range(1, N+1)]
result1 = list(combinations(items,M))

for x in result1:
    for y in range(M):
        print(x[y],end=" ")
    print(end="\n")
