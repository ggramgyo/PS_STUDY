opp = ['+', '-', '*', '/']
for testcase in range(1, 11):
    N = int(input())
    flag = True
    for _ in range(N):
        query = list(input().rstrip().split())
        if len(query) == 2:
            node, value = query
            if value in opp:
                flag = False
        elif len(query) >= 3:
            _, a, b = query[0], query[1], query[:]
            if a not in opp:
                flag = False
                
    print("#{} {}".format(testcase, int(flag)))