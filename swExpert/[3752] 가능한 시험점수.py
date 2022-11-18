tc = int(input())
for testcase in range(1, tc+1):
    N = int(input())
    ans = set()
    ans.add(0)
    ps = list(map(int, input().split()))
    for p in ps:
        tmp = list(set(ans))
        for a in tmp:
            ans.add(a+p)
    print("#{} {}".format(testcase, len(ans)))