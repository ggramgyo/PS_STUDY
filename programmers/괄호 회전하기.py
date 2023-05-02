from collections import deque

match = {")": "(", "]": "[", "}": "{"}


def is_valid(s):
    stack = []
    for char in s:
        if char in match:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack


def solution(s):
    if len(s) % 2 != 0:
        return 0

    q = deque(s)
    count = 0
    for i in range(len(s)):
        if is_valid(q):
            count += 1
        q.rotate(1)
    return count