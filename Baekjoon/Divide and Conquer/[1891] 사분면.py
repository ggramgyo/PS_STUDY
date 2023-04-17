import sys


def find_target(nx, ny, l, k):
    global d
    if l == 0:
        return nx, ny
    if word[k] == '1':
        return find_target(nx + l, ny + l, l//2, k+1)
    elif word[k] == '2':
        return find_target(nx, ny + l, l//2, k+1)
    elif word[k] == '3':
        return find_target(nx, ny, l//2, k+1)
    elif word[k] == '4':
        return find_target(nx + l, ny, l//2, k+1)


def find_answer(nx, ny, ans, l):
    if l == 0:
        return ans
    # 1
    if l <= nx < 2 *l and l <= ny < 2 * l:
        return find_answer(nx-l, ny-l, ans+'1', l//2)
    # 2
    elif 0 <= nx < l and l <= ny < l * 2:
        return find_answer(nx, ny-l, ans + '2', l // 2)
    # 3
    elif 0 <= nx < l and 0 <= ny < l:
        return find_answer(nx, ny, ans+'3', l//2)
    # 4
    elif l <= nx < l * 2 and 0 <= ny < l:
        return find_answer(nx - l, ny, ans+'4', l//2)


d, word = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())
word = str(word)
nx, ny = find_target(0, 0, 2**(d-1), 0)
nx += x
ny += y
print(find_answer(nx, ny, '', 2**(d-1))) if 0 <= nx < 2**d and 0 <= ny < 2**d else print(-1)
