tc = int(input())
for testcase in range(1, tc+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    answer = 0
    for i in range(1, N+1):
        tmp = i
        if i > N // 2 + 1:
            i = N+1 - i
        w = 2 * i - 1
        start = (N-w)//2
        for j in range(start, start+w):
            answer += graph[tmp-1][j]
    print("#{} {}".format(testcase, answer))