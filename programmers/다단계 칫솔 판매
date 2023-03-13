from collections import defaultdict


def solution(enroll, referral, seller, amount):
    tree = {}
    n = len(enroll)
    value = defaultdict(int)
    for i in range(n):
        tree[enroll[i]] = referral[i]

    m = len(seller)
    for i in range(m):
        start = seller[i]
        init_value = amount[i] * 100
        while start != '-':
            if init_value < 1:
                break
            tmp_value = (init_value // 10)
            value[start] += (init_value - tmp_value)
            init_value = tmp_value
            start = tree[start]
        value['-'] += init_value
    result = []
    for i in range(n):
        result.append(value[enroll[i]])
    return result
