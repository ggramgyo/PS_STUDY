import sys

h, w = map(int, sys.stdin.readline().split())
graph = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(1, w-1):
    # 왼쪽에서 max height
    max_left_height = max(graph[:i])
    # 오론쪽에서 max height
    max_right_height = max(graph[i+1:])
    # 해당 i에서 차오를 수 있는 maximum 은 위 두 값 중 min 값
    i_max_height = min(max_left_height, max_right_height)
    if i_max_height > graph[i]:
        ans += i_max_height - graph[i]
print(ans)

