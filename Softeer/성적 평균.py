import sys

N, K = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    tmp = round(sum(scores[a-1:b])/(b-a+1), 2)
    if str(tmp)[-1] == '0':
        print(str(tmp)+'0')
    else:
        print(tmp)