import itertools
from copy import deepcopy


def solution(beginning, target):
    row = len(beginning)
    answer = 2**(2*row)
    flips = [0, 1]
    col = len(beginning[0])
    # itertools product 이용해 (1) 뒤집음 (2) 안 뒤집음 경우의 수 나눠줌
    for flip in itertools.product(flips, repeat=row):
        flip_beginning = deepcopy(beginning)
        # check row
        for i in range(row):
            flip_beginning[i] = [(r+1)%2 if flip[i] else r for r in flip_beginning[i]]
        flag = True
        # check column
        c = 0
        for i in range(col):
            cnt = 0
            if flag:
                for j in range(row):
                    if flip_beginning[j][i] != target[j][i]:
                        cnt += 1
                if cnt and cnt != col:
                    flag = False
                    break
            if cnt == col:
                c += 1
        if flag:
            answer = min(answer, sum(flip) + c)
    # 코드가 더러운 거 같다. 다른 풀이방법으로 참고해서 풀어봐야 겠다
    return answer if answer != 2**(2*row) else -1
