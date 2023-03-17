from itertools import permutations


def check(user,ban):
    for i in range(len(ban)):
        if len(ban[i]) != len(user[i]):
            return False
        for j in range(len(ban[i])):
            if ban[i][j] == "*":
                continue
            elif ban[i][j] != user[i][j]:
                return False
    return True
# 참고
def solution(user_id, banned_id):
    answer = []
    # 조건이 작아 permutation 이용
    for user_cases in list(permutations(user_id, len(banned_id))):
        if check(user_cases, banned_id):
            # 조건 탐색 후 중복 제거
            if set(user_cases) not in answer:
                answer.append(set(user_cases))
    return len(answer)
