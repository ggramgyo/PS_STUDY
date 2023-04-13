import heapq
from collections import deque


def solution(sequence, k):
    result = []
    answer = deque()
    left = 0
    s = 0
    for right in range(len(sequence)):
        s += sequence[right]
        answer.append(sequence[right])
        if s == k:
            heapq.heappush(result, [len(answer), [left, right]])
        while k <= s:
            s -= sequence[left]
            left += 1
            answer.popleft()
            if s == k:
                heapq.heappush(result, [len(answer), [left, right]])
    return heapq.heappop(result)[1]
