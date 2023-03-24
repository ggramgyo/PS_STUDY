kind = {(0, 'diamond'): 1, (0, 'iron'): 1, (0, 'stone'): 1,(1, 'diamond'): 5, (1, 'iron'): 1, (1, 'stone'): 1,(2, 'diamond'): 25, (2, 'iron'): 5, (2, 'stone'): 1}

def solution(picks, minerals):
    answer = 0
    measure = []
    possible_minerals = sum(picks) * 5

    for x in range(0, len(minerals), 5):
        # 가진 곡괭이로 팔 수 있는 최대 미네랄
        if x < possible_minerals:
            d, i, s = 0, 0, 0
            for y in range(5):
                # ix error 고려
                if x + y < len(minerals):
                    d += kind[(0, minerals[x+y])]
                    i += kind[(1, minerals[x+y])]
                    s += kind[(2, minerals[x+y])]
            # 가중치 dis
            measure.append((d+i+s, d, i, s))
    measure.sort()
    for x in range(3):
        # 가중치가 높을수록 다이아로 캐야 유리
        # Greedy 사용 
        if picks[x] and measure:
            answer += measure.pop()[x+1]
            picks[x] -= 1
    return answer
