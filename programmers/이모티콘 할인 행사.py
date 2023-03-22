import itertools

def solution(users, emoticons):
    answer = []
    sales = [10, 20, 30, 40]
    # 각각의 이모티콘 할인율을 적용해주기 위해서 itertools.product 사용
    #(10, 10), (10, 20), ... (20, 10), (20, 20), .... (40, 30), (40, 40)
    for sale in itertools.product(sales, repeat=len(emoticons)):
        # 이모티콘 플러스 가입 수, 가입한 사람 제외 한 total 값
        enter_plus = 0
        total = 0
        for user in users:
            # user의 이모티콘 플러스 가입 기준을 따지기 위해 user_value 선언
            user_value = 0
            li, li_plus = user
            # user 마다 할인율을 적용해서 계산
            for i in range(len(emoticons)):
                # 제한 할인율 따짐.
                if li <= sale[i]:
                    user_value += ((100 - sale[i]) * emoticons[i]) // 100
            # 이모티콘 플러스 가입 조건 따짐.
            if user_value >= li_plus:
                enter_plus += 1
            else:
                total += user_value
        answer.append((enter_plus, total))
    # answer list를 (1) 이모티콘 가입자 수, (2) total 값 (다중 조건)으로 정렬해줌.
    answer.sort(key=lambda x:(-x[0],-x[1]))
    return list(answer[0])
