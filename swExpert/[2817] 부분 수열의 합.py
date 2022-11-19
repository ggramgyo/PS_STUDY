def dfs(i, t):
    global total, count
    if t > K:
        return
    if total - t < K - t:
        return
    if t == K:
        count += 1
        return
    if i >= N:
        if t == K:
            count += 1
        return
    dfs(i+1, t+number[i])
    dfs(i+1, t)


tc = int(input())
for testcase in range(1, tc+1):
    N, K = map(int, input().split())
    number = list(map(int, input().split()))
    total = sum(number)
    count = 0
    dfs(0, 0)
    print("#{} {}".format(testcase, count))