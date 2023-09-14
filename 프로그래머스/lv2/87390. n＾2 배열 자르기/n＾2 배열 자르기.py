def solution(n, left, right):
    answer = []
    # left, right for문으로 돌면서 index 값 정의
    for target in range(left, right+1):
        i = target // n + 1
        j = target % n + 1
        target = i if i > j else j
        answer.append(target)
        
    return answer