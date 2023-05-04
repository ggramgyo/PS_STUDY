import sys
from collections import defaultdict, deque

N = int(sys.stdin.readline())
nums = set(map(int, sys.stdin.readline().split()))
store = defaultdict(int)
start = 0
for num in nums:
    check = 0
    if not num%3 and num//3 in nums:
        store[num//3] = num
        check += 1
    if num * 2 in nums:
        store[num*2] = num
        check += 1
    if not check:
        start = num

answer = deque()
while True:
    answer.appendleft(start)
    if not store[start]:
        break
    start = store[start]
print(*answer)

