NUMBER_MAX = 10
MAX = 100001

# 자판 이동 비용을 미리 구해놓음
steps = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
         [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
         [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
         [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
         [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
         [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
         [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
         [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
         [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
         [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]

# DP
# numbers.length, 왼손가락, 오른손가락이 위치한 숫자
cache = [[[-1] * NUMBER_MAX for _ in range(NUMBER_MAX)] for _ in range(MAX)]

def func(idx, left, right, copyNumbers):
    if idx == len(copyNumbers):
        return 0
    print(idx, left, right, copyNumbers)
    result = cache[idx][left][right]
    print(result)
    if result != -1:
        return result

    cur = int(copyNumbers[idx])

    # 현재 손가락이 자판에 위치하면 비용은 1
    if left == cur or right == cur:
        result = 1 + func(idx + 1, left, right, copyNumbers)
    else:
        # 왼손가락 혹은 오른손가락이 움직였을 때
        result = min(func(idx + 1, cur, right, copyNumbers) + steps[left][cur],
                     func(idx + 1, left, cur, copyNumbers) + steps[right][cur])

    cache[idx][left][right] = result
    return result


def solution(numbers):
    global cache
    return func(0, 4, 6, numbers)

solution("1756")