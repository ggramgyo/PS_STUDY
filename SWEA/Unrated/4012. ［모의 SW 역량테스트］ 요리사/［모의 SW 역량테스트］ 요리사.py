import itertools

T=int(input())
for testcase in range(1, T+1):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    maximum = sum([sum(f) for f in food])
    nums = [i for i in range(N)]
    answer = float('inf')
    for li in itertools.combinations(nums, N//2):
        a, b = 0, 0
        temp = []
        for l in nums:
            if l not in set(li):
                temp.append(l)
        for l in itertools.combinations(li, 2):
            x, y = l
            a += food[x][y] + food[y][x]
        for l in itertools.combinations(temp, 2):
            x, y = l
            b += food[x][y] + food[y][x]
        answer = min(answer, abs(a-b))
    print("#{} {}".format(testcase, answer))