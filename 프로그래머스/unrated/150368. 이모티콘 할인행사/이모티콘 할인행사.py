percentage = [10, 20, 30, 40]
pm = []
MAX_SIGN_COUNT = 0
MAX_TOTAL_MONEY = 0


def cal(emoticons, users, limit):
    SIGN_COUNT = 0
    TOATL_MONEY = 0
    for user in users:
        pl, ml = user
        tmp = 0
        for i in range(limit):
            if percentage[pm[i]] >= pl:
                tmp += int(emoticons[i] * ((100 - percentage[pm[i]]) * 0.01))
        if tmp >= ml:
            SIGN_COUNT += 1
        else:
            TOATL_MONEY += tmp
    return (SIGN_COUNT, TOATL_MONEY)


def permutation(ix, limit, emoticons, users):
    global MAX_SIGN_COUNT, MAX_TOTAL_MONEY
    if ix == limit:
        SIGN_COUNT, TOATL_MONEY = cal(emoticons, users, limit)
        if SIGN_COUNT > MAX_SIGN_COUNT:
            MAX_SIGN_COUNT = SIGN_COUNT
            MAX_TOTAL_MONEY = TOATL_MONEY
        elif SIGN_COUNT == MAX_SIGN_COUNT:
            MAX_TOTAL_MONEY = max(MAX_TOTAL_MONEY, TOATL_MONEY)

        return

    for i in range(4):
        pm.append(i)
        permutation(ix + 1, limit, emoticons, users)
        pm.pop()


def solution(users, emoticons):
    global MAX_SIGN_COUNT, MAX_TOTAL_MONEY
    limit = len(emoticons)
    permutation(0, limit, emoticons, users)
    return [MAX_SIGN_COUNT, MAX_TOTAL_MONEY]
