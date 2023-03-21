def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []
    for i in range(len(numbers)):
        if len(stack):
            # 큰 수 찾아줄 때까지 pop
            while stack and stack[-1][0] < numbers[i]:
                answer[stack[-1][1]] = numbers[i]
                stack.pop()
        stack.append((numbers[i], i))
    return answer