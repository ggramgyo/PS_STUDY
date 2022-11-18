from collections import deque

for testcase in range(1, 11):
    tc = int(input())
    pw = list(map(int, input().split()))
    q = deque(pw)
    t = 1
    while True:
        s = q.popleft()
        q.append(s-t)
        t = (t + 1) % 6
        t = 1 if not t else t
        if q[-1] <= 0:
            q[-1] = 0
            break
    print("#{} {} {} {} {} {} {} {} {}".format(testcase, *q))