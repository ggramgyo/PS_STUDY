def solution(s):
    return str(min(list(map(int, s.split(" "))))) + ' ' +  str(max(list(map(int, s.split(" ")))))

solution("-1 -2 -3 -4")