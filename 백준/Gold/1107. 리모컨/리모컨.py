import sys
from itertools import product

target = int(sys.stdin.readline())

N = int(sys.stdin.readline())
possibleBtn = []
if N:
    breakBtn = set(map(int, sys.stdin.readline().split()))
    for i in range(10):
        if i not in breakBtn:
            possibleBtn.append(i)
else:
    possibleBtn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = abs(target - 100)

for length in range(max(1, len(str(target))-1), len(str(target))+2):
    for makeNum in product(possibleBtn, repeat=length):
        makeNumStr = "".join(map(str, makeNum))
        makeNumInt = int(makeNumStr)
        answer = min(answer, abs(makeNumInt - target) + len(makeNumStr))

print(answer)