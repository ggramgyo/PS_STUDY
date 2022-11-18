def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        root[b] = a
    else:
        root[a] = b


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    d = float(input())
    e = []
    for i in range(N):
        for j in range(i+1, N):
            # if i != j:
            e.append((i, j, ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) * d))
    e.sort(key=lambda z: z[2])
    # print(e)
    root = [x for x in range(N)]
    edge = 0
    cost = 0
    while True:
        if edge == N-1:
            break
        u, v, w = e.pop(0)
        if find(u) != find(v):
            union(u, v)
            cost += w
            edge += 1

    print("#{} {}".format(test_case, round(cost)))




