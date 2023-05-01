# 문제가 이해가 안 가 참고했다. 그냥 이해안가는 상태로 푸는게 난 거 같다.
def check(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def div(p):
    l, r = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            return p[:i+1], p[i+1:]


def solution(p):
    if not p:
        return ""
    u, v = div(p)
    # u가 올바른 괄호 문자열 이라면
    if check(u):
        return u + solution(v)
    # u가 올바른 괄호가 아니라면
    else:
        tmp = '(' + solution(v) + ')'
        for i in u[1:-1]:
            if i == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp


