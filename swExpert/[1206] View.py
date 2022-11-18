for testcase in range(1, 11):
    result = 0
    N = int(input())
    house = list(map(int , input().split()))
    for i in range(2, N-2):
        m = max(house[i-1],house[i-2],house[i+1],house[i+2])
        if house[i] > m:
            result += (house[i] - m)

    print("#{} {}".format(testcase,result))