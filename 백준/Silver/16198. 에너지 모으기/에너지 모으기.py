import sys


def bt(total):
    global answer
    # 종료 구간
    if len(e) == 2:
        answer = max(answer, total)
    # pop index 고려해서 len() 사용
    for i in range(1, len(e) - 1):
        energy = e[i - 1] * e[i + 1]
        temp = e.pop(i)
        bt(total + energy)
        e.insert(i, temp)


N = int(sys.stdin.readline())
e = list(map(int, sys.stdin.readline().split()))
answer = float('-inf')
bt(0)
print(answer)
