import sys

N, M, L, K = map(int, sys.stdin.readline().split())
stars = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
t = len(stars)
max_cnt = 0
for x in range(t):
    for y in range(t):
        # i.x, j.y
        cnt = 0
        for z in range(t):
            if stars[x][0] <= stars[z][0] <= stars[x][0] + L and stars[y][1] <= stars[z][1] <=stars[y][1]+L:
                cnt += 1
        max_cnt = max(cnt, max_cnt)
print(len(stars) - max_cnt)

# https://velog.io/@dot2__/BOJ-14658%EB%B2%88-%ED%95%98%EB%8A%98%EC%97%90%EC%84%9C-%EB%B3%84%EB%98%A5%EB%B3%84%EC%9D%B4-%EB%B9%97%EB%B0%9C%EC%B9%9C%EB%8B%A4-Java
# 면적에 별똥별이 포함되는지 여부의 최댓값을 이런식으로 구할지는 생각을 못했다.
# 다음번에 비슷한 문제가 나온다면 비슷한 방식으로 풀 수 있을 거 같다. 위 블로그 보고 이해하는데 도움이 많이 됐다.