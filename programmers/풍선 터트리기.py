# 인접한 두 풍선 중 터트릴 것을 고른다.
# 번호가 더 작은것을 고를 기회는 한번 뿐
# 날렸다면 다음부턴 무조건 큰 거
# 왼쪽 오른쪽 각각 최소값을 갱신해서 저장하면?


def solution(a):
    answer = 0
    min_dp = [float('inf')] * len(a)
    min_dp[0] = a[0]
    # 왼쪽부터 최솟값 갱신
    for i in range(1, len(a)):
        min_dp[i] = min(min_dp[i-1], a[i])
    print(min_dp)
    # 오른쪽부터 탐색 시작하는 오른쪽은 다시 갱신하면서
    # 양 쪽이랑 값 비교했을 때 한번은 커도 된다. 두번은 x
    # a list 양 끝은 무조건 살아남음
    min_dp[-1] = a[-1]
    for i in range(len(a)-2,0, -1):
        # a i값이 왼, 오 둘 다보다 작다면 통과
        if a[i] < min_dp[i-1] and a[i] < min_dp[i+1]:
            answer += 1
        # a i값이 왼, 오 하나보단 큰 경우도 통과
        elif (min_dp[i - 1] < a[i] < min_dp[i + 1]) or (min_dp[i - 1] > a[i] > min_dp[i + 1]):
            answer += 1
        # a i값이 왼, 오 둘 다 보다 큰 경우는 안됨.
        else:
            pass
        # 오른쪽 값은 계속 갱신해줘야된다.
        min_dp[i] = min(min_dp[i+1], a[i])
    return answer + 2


# 위 코드는 통과는 되지만 시간이 너무 심각하다.
# https://velog.io/@eehwan/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%92%8D%EC%84%A0-%ED%84%B0%ED%8A%B8%EB%A6%AC%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 참고해서 푼 풀이 적용해보면 확실히 빨라진 것이 보인다.
# 왼, 오 동시 탐색 two-point

def solution2(a):
    result = [False] * len(a)
    min_front = float('inf')
    min_back = float('inf')

    for i in range(len(a)):
        if a[i] < min_front:
            min_front = a[i]
            result[i] = True
        if a[-1-i] < min_back:
            min_back = a[-1-i]
            result[-1-i] = True
    return sum(result)

