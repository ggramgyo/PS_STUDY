from math import log2
import sys
sys.setrecursionlimit(10**5)

def check_tree(i, s):
    # 탈출 조건
    if len(s) == 1:
        return True
    if s[i] == '0':
        # 0 노드라해서 무조건 False 넣었다가 틀림. 자식 노드들이 다 0이면 True 
        if not all(c == '0' for c in s):
            return False
    return check_tree(i//2, s[:i]) and check_tree(i//2, s[i+1:])

def solution(numbers):
    answer = []
    for number in numbers:
        binary_number = str(bin(number)[2:])
        # 포화 이진트리 요소 개수 맞추기 위해 앞에 0 추가
        d = 2 ** (int(log2(len(binary_number))) + 1) - 1
        binary_number = '0' * (d - len(binary_number)) + binary_number
        # 재귀로 가능 유무를 따짐.
        if check_tree(len(binary_number)//2, binary_number):
            answer.append(1)
        else:
            answer.append(0)
    return answer