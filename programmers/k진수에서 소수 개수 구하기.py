import math


def convert(num, base):
    tmp = ''
    while num:
        tmp = str(num % base) + tmp
        num //= base
    return tmp


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    for cn in convert(n, k).split('0'):
        if cn and is_prime(int(cn)):
            answer += 1
    return answer
