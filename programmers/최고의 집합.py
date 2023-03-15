def solution(n, s):
    if n > s:
        return [-1]
    m = s // n
    answer = [m for _ in range(n)]
    start, ix = m * n, n-1
    while start != s:
        answer[ix] += 1
        ix = n-1 if ix == 0 else ix - 1
        start += 1
    return answer