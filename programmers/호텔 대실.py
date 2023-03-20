from collections import defaultdict


def time2val(s, e):
    return int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])

def solution(book_time):
    check = defaultdict(int)
    for bt in book_time:
        start, end = bt
        ns, ne = time2val(start, end)
        for i in range(ns, ne+10):
            check[i] += 1

    return max(check.values())
