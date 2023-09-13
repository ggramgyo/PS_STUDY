from collections import deque
def solution(queue1, queue2):
    q1 = sum(queue1)
    q2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    while q1 != q2:
        if answer > 10000000:
            answer = -1
            break
        # q2가 더 크다면 q2에서 빼주고
        while q1 < q2:
            value = queue2.popleft()

            q2 -= value
            q1 += value

            queue1.append(value)

            answer += 1
        # q1가 더 크다면 q1에서 빼주고
        while q2 < q1:
            value = queue1.popleft()

            q1 -= value
            q2 += value

            queue2.append(value)
        
            answer += 1
        
    print(q1, q2)
    return answer