import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    p = [0] + list(map(int, sys.stdin.readline().split()))
    check = [False] * (n + 1)
    result = []
    for i in range(1, n + 1):
        if not check[i]:
            cycle = []
            start = i
            while True:
                if check[start]:
                    if start in cycle:
                        result += cycle[cycle.index(start):]
                    break
                cycle.append(start)
                check[start] = True
                start = p[start]
    print(n - len(result))
