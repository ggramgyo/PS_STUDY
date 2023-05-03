from collections import defaultdict


def solution(gems):
    answer = []
    # 어떤 보석 소유 확인
    is_own = defaultdict(int)
    for i in range(len(gems)):
        is_own[gems[i]] += 1
    is_check = defaultdict(int)
    is_own_total = len(is_own)
    back = 0
    check_count = 0
    for i in range(len(gems)-is_own_total+1):
        # 앞에서 차근차근 빼주면서 카운트 줄어들면 다음 다시 탐색
        if i >= 1:
            is_check[gems[i-1]] -= 1
            if not is_check[gems[i-1]]:
                check_count -= 1

        # 탐색을 하고 가장 가까운 곳에서 멈추게 됨.
        while check_count != is_own_total:
            if back >= len(gems):
                break
            if not is_check[gems[back]]:
                check_count += 1
            is_check[gems[back]] += 1
            back += 1
        if check_count == is_own_total:
            answer.append([abs(back-1-i), i+1, back])
    answer.sort(key=lambda x: [x[0], x[1]])
    return answer[0][1:]
