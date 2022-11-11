from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    res = s1 + s2
    if res % 2 == 1:
        return -1
    ans = 0
    limit = len(queue1) + len(queue2)
    res //= 2
    while s1 != s2:
        if ans >= limit * 4:
            return -1
        while res < s1:
            s1 -= queue1[0]
            s2 += queue1[0]
            queue2.append(queue1.popleft())
            ans += 1
        while res < s2:
            s2 -= queue2[0]
            s1 += queue2[0]
            queue1.append(queue2.popleft())
            ans += 1
    return ans