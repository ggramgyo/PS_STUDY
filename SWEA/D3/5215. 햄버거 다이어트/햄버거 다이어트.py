def bt(i, taste, calorie):
    global N, answer, L
    # 종료조건 1
    if calorie > L:
        return
    # 종료조건 2
    if i >= N:
        answer = max(answer, taste)
        return
    bt(i+1, taste + k[i][0], calorie + k[i][1])
    bt(i+1, taste, calorie)


T=int(input())
for testcase in range(1, T+1):
    N, L = map(int, input().split())
    answer = float('-inf')
    k = [list(map(int, input().split())) for _ in range(N)]
    bt(0, 0, 0)
    print("#{} {}".format(testcase, answer))