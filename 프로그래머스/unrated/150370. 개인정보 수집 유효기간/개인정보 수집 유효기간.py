"2011.12.18", ["A 13"], ["2001.01.01 A", "2010.11.28 A"]

def solution(today, terms, privacies):
    answer = []
    contract = {}
    ty, tm, td = map(int, today.split("."))
    for term in terms:
        kind, period = term.split()
        contract[kind] = int(period)
        
    for i in range(len(privacies)):
        date, kind = privacies[i].split()
        cy, cm, cd = map(int, date.split("."))
        cy = cy + (cm + contract[kind]) // 12
        cm = (cm + contract[kind]) % 12
        if cm == 0:
            cm = 12
            cy -= 1
        if cy - ty < 0 or (cy - ty <= 0 and cm - tm < 0) or (cy - ty <= 0 and cm - tm <= 0 and cd - td <= 0):
            answer.append(i+1)
            
        
        
    return answer