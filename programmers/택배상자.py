# 4, 3, 1, 2, 5 기사 원하는 순서
# 1, 2, 3, 4, 5 영수가 받는 순서
# --------------
# [3, 2, 1]
# [4]
# --------------
# [2, 1]
# [4, 3] 1을 실어야 되지만 2가 있어 여기서 stop -> result : 2
from collections import deque


def solution(order):
    answer = 0
    l = len(order)
    boxes, order = deque([i for i in range(1, l+1)]), deque(order)
    tmp_boxes = []

    while boxes:
        now_box = boxes.popleft()
        # 지금 박스와 order[0] 같다면 popleft
        if now_box == order[0]:
            answer += 1
            order.popleft()
            if not boxes and tmp_boxes:
                boxes.append(tmp_boxes.pop())
        # 아니라면 임시 박스 우선 확인 후 여기도 없다면 넣음
        else:
            if tmp_boxes and tmp_boxes[-1] == order[0]:
                tmp_boxes.pop()
                order.popleft()
                boxes.appendleft(now_box)
                answer += 1
            else:
                tmp_boxes.append(now_box)

    return answer
