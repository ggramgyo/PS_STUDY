N, K = map(int, input().split())
num = list(input().rstrip())
stack = []
k = K
for i in range(N):
    print(i)
    while k > 0 and stack and stack[-1] < num[i]:
        print(stack)
        stack.pop()
        k -= 1
    stack.append(num[i])
print(''.join(stack[:N-K]))

