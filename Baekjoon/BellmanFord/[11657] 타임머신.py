import sys


def bellman_ford(start, N, M):
    # 시작 노드 초기화
    city[start] = 0
    # 전체 반복
    for i in range(N):
        # 매 반복에 모든 간선 조회
        for j in range(M):
            s, e, v = edges[j]
            # s -> e 이동 거리가 더 짧은 경우
            if city[s] != INF and city[e] > city[s] + v:
                city[e] = city[s] + v
                # ★ N번째 노드에서 역시 값이 갱신된 경우 음수 순환이 존재
                if i == N - 1:
                    return True
    return False


INF = int(1e9)
N, M = map(int, sys.stdin.readline().split())
city = [INF] * (N+1)
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

if not bellman_ford(1, N, M):
    for i in range(2, N+1):
        if city[i] == INF:
            print(-1)
        else:
            print(city[i])
else:
    print(-1)