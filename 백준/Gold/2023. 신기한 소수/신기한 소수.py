import sys


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def bt(num):
    global N
    if len(str(num)) == N:
        print(num)

    for i in range(1, 10):
        temp = num * 10 + i
        if isPrime(temp):
            bt(temp)


N = int(sys.stdin.readline())
for start in [2, 3, 5, 7]:
    bt(start)
