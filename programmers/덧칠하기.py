def solution(n, m, section):
    answer = 0
    start = 0
    flag = False
    for s in section:
        if start <= s:
            if start + m <= n:
                answer += 1
                start = s + m
            else:
                flag = True
                break
    
    return answer + 1 if flag else answer
