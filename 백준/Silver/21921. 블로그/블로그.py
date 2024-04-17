import sys

N, X = map(int, sys.stdin.readline().split())
visit = list(map(int, sys.stdin.readline().split()))

init = sum(visit[:X]) 
answer = init
count = 1  

for i in range(X, N):
    init -= visit[i - X]  
    init += visit[i]  

    if answer < init:
        answer = init
        count = 1
    elif answer == init:
        count += 1

if answer > 0:
    print(answer)
    print(count)
else:
    print('SAD')
